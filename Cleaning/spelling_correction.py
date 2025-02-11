import os
import pandas as pd
from tqdm import tqdm
from transformers import pipeline
from datasets import Dataset

from config import MODEL_NAME, \
                    MODEL_TYPE, \
                    MAX_LENGTH, \
                    BATCH_SIZE, \
                    COLUMN_NAME_AFTER_CLEAN

# Khởi tạo pipeline sửa lỗi chính tả
corrector = pipeline(MODEL_TYPE, model=MODEL_NAME)

def spelling_correction(model_input_folder, model_output_folder):
    """
    - Duyệt các file chunk trong model_input_folder.
    - Đọc dữ liệu, loại bỏ các hàng có giá trị NaN ở cột COLUMN_NAME_AFTER_CLEAN.
    - Sử dụng Hugging Face Dataset để batch process qua hàm map và gọi corrector.
    - Lưu file đã xử lý vào model_output_folder.
    - Xóa file gốc sau khi đã xử lý.
    - Hiển thị thanh tiến trình và log thông tin số chunk đang xử lý.
    """
    # Đảm bảo thư mục output tồn tại
    if not os.path.exists(model_output_folder):
        os.makedirs(model_output_folder)

    # Lấy danh sách file CSV trong thư mục input và sắp xếp
    chunk_files = sorted(os.listdir(model_input_folder))
    total_chunks = len(chunk_files)

    # Sử dụng tqdm để theo dõi tiến trình
    with tqdm(total=total_chunks, desc="Spelling Correction") as pbar:
        for i, chunk_file in enumerate(chunk_files):
            pbar.set_postfix_str(f"Processing chunk {i+1}/{total_chunks}")
            input_path = os.path.join(model_input_folder, chunk_file)
            output_path = os.path.join(model_output_folder, chunk_file)

            try:
                # Đọc file CSV và xử lý dữ liệu
                df = pd.read_csv(input_path)
                df = df.dropna(subset=[COLUMN_NAME_AFTER_CLEAN])
                df[COLUMN_NAME_AFTER_CLEAN] = df[COLUMN_NAME_AFTER_CLEAN].astype(str)
                texts = df[COLUMN_NAME_AFTER_CLEAN].tolist()

                # Chuyển danh sách text thành Dataset
                ds = Dataset.from_dict({"text": texts})

                # Định nghĩa hàm map dùng để gọi pipeline cho batch các text
                def correction_function(batch):
                    # Lưu ý: batch["text"] là danh sách các text được xử lý cùng lúc
                    predictions = corrector(
                        batch["text"],
                        max_length=MAX_LENGTH,
                        batch_size=BATCH_SIZE  # hoặc có thể điều chỉnh batch_size tại đây
                    )
                    corrected_texts = [pred["generated_text"] for pred in predictions]
                    return {"corrected_text": corrected_texts}

                # Áp dụng map để sửa lỗi theo batch
                ds = ds.map(correction_function, batched=True, batch_size=8)

                # Gán kết quả đã sửa vào DataFrame
                df[COLUMN_NAME_AFTER_CLEAN] = ds["corrected_text"]

                # Lưu file đã xử lý vào thư mục output
                df.to_csv(output_path, index=False, encoding="utf-8")

                # Xóa file chunk gốc sau khi đã xử lý
                os.remove(input_path)

            except Exception as e:
                print(f"Error processing {chunk_file}: {e}")

            pbar.update(1)
