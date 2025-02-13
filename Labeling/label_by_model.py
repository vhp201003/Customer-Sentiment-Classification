import os
import pandas as pd
from tqdm import tqdm
from transformers import pipeline
from datasets import Dataset

from config import MODEL_NAME, \
                    MODEL_TYPE, \
                    COLUMN_NAME_TO_LABEL, \
                    COLUMN_NAME_LABEL

# Khởi tạo pipeline Zero-Shot Classification
classifier = pipeline(MODEL_TYPE, model=MODEL_NAME)

def label_by_model(input_folder, output_folder, labels):
    """Gán nhãn dữ liệu bằng Zero-Shot Classification."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    chunk_files = sorted(os.listdir(input_folder))
    total_chunks = len(chunk_files)
    
    with tqdm(total=total_chunks, desc="Zero-Shot Labeling") as pbar:
        for i, chunk_file in enumerate(chunk_files):
            pbar.set_postfix_str(f"Processing chunk {i+1}/{total_chunks}")
            input_path = os.path.join(input_folder, chunk_file)
            output_path = os.path.join(output_folder, chunk_file)
            
            try:
                df = pd.read_csv(input_path)
                df = df.dropna(subset=[COLUMN_NAME_TO_LABEL])
                df[COLUMN_NAME_TO_LABEL] = df[COLUMN_NAME_TO_LABEL].astype(str)
                texts = df[COLUMN_NAME_TO_LABEL].tolist()
                
                # Chuyển danh sách text thành Dataset
                ds = Dataset.from_dict({"text": texts})
                
                # Hàm gán nhãn với Zero-Shot Classification
                def labeling_function(batch):
                    predictions = classifier(
                        batch["text"],
                        candidate_labels=labels,
                        multi_label=False  # Chọn True nếu muốn gán nhiều nhãn
                    )
                    return {COLUMN_NAME_LABEL: [pred["labels"][0] for pred in predictions]}
                
                # Áp dụng Zero-Shot Classification theo batch
                ds = ds.map(labeling_function, batched=True, batch_size=8)
                
                # Gán kết quả vào DataFrame
                df[COLUMN_NAME_LABEL] = ds[COLUMN_NAME_LABEL]
                
                # Lưu file đã xử lý
                df.to_csv(output_path, index=False, encoding="utf-8")
                
                # Xóa file chunk gốc
                os.remove(input_path)
            except Exception as e:
                print(f"Error processing {chunk_file}: {e}")
            
            pbar.update(1)

if __name__ == "__main__":
    LABELS = ["tích cực", "tiêu cực", "trung lập"]  # Danh sách nhãn
    INPUT_FOLDER = "/kaggle/working/chunked_label_data/"
    OUTPUT_FOLDER = "/kaggle/working/labeled_chunks/"
    zero_shot_labeling(INPUT_FOLDER, OUTPUT_FOLDER, LABELS)
