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
classifier = pipeline(
    MODEL_TYPE, 
    model=MODEL_NAME, 
    tokenizer=MODEL_NAME
)

def label_by_model(input_folder, output_folder):
    """Gán nhãn dữ liệu bằng mô hình Sentiment-Analysis."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    chunk_files = sorted(os.listdir(input_folder))
    total_chunks = len(chunk_files)
    
    with tqdm(total=total_chunks, desc="Sentiment Labeling") as pbar:
        for i, chunk_file in enumerate(chunk_files):
            pbar.set_postfix_str(f"Processing chunk {i+1}/{total_chunks}")
            input_path = os.path.join(input_folder, chunk_file)
            output_path = os.path.join(output_folder, chunk_file)
            
            try:
                df = pd.read_csv(input_path)
                # Bỏ dòng NaN
                df = df.dropna(subset=[COLUMN_NAME_TO_LABEL])
                df[COLUMN_NAME_TO_LABEL] = df[COLUMN_NAME_TO_LABEL].astype(str)
                texts = df[COLUMN_NAME_TO_LABEL].tolist()
                
                # Chuyển dữ liệu thành Dataset
                ds = Dataset.from_dict({"text": texts})
                
                # Hàm gán nhãn với Sentiment Analysis
                def labeling_function(batch):
                    predictions = classifier(batch["text"])
                    # predictions thường là list các dict: [{"label": "POSITIVE", "score": 0.987}, ...]
                    mapped_labels = []
                    for pred in predictions:
                        label = pred["label"].upper()  # Chuyển thành chữ in hoa để so sánh dễ hơn
                        if "POS" in label:       # Có thể là 'POSITIVE' hay 'POS'
                            mapped_labels.append("tích cực")
                        elif "NEG" in label:     # Có thể là 'NEGATIVE' hay 'NEG'
                            mapped_labels.append("tiêu cực")
                        else:
                            mapped_labels.append("trung lập")
                    return {COLUMN_NAME_LABEL: mapped_labels}
                
                # Áp dụng sentiment-analysis theo batch
                ds = ds.map(labeling_function, batched=True, batch_size=8)
                
                # Đưa kết quả vào DataFrame
                df[COLUMN_NAME_LABEL] = ds[COLUMN_NAME_LABEL]
                
                # Lưu file đã xử lý
                df.to_csv(output_path, index=False, encoding="utf-8")
                
                # Xoá file chunk gốc sau khi gán nhãn xong (tuỳ ý)
                os.remove(input_path)
            except Exception as e:
                print(f"Error processing {chunk_file}: {e}")
            
            pbar.update(1)

if __name__ == "__main__":
    LABELS = ["tích cực", "tiêu cực", "trung lập"]  # Danh sách nhãn
    INPUT_FOLDER = "/kaggle/working/chunked_label_data/"
    OUTPUT_FOLDER = "/kaggle/working/labeled_chunks/"
    zero_shot_labeling(INPUT_FOLDER, OUTPUT_FOLDER, LABELS)
