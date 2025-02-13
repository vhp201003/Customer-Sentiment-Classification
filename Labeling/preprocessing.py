import os
import pandas as pd
from config import COLUMN_NAME_TO_LABEL

def preprocessing(input_file, output_folder, output_file_name):
    """Tiền xử lý dữ liệu: loại bỏ dòng trống, dữ liệu trùng lặp và lưu kết quả."""
    if not os.path.exists(input_file):
        print(f"Lỗi: File '{input_file}' không tồn tại.")
        return

    os.makedirs(output_folder, exist_ok=True)  # Tạo thư mục nếu chưa có

    try:
        df = pd.read_csv(input_file)
        
        # Kiểm tra cột có tồn tại không
        if COLUMN_NAME_TO_LABEL not in df.columns:
            print(f"Lỗi: Cột '{COLUMN_NAME_TO_LABEL}' không tồn tại trong dữ liệu.")
            return
        
        df = df[[COLUMN_NAME_TO_LABEL]].dropna().drop_duplicates().reset_index(drop=True)
        output_path = os.path.join(output_folder, output_file_name)
        df.to_csv(output_path, index=False, encoding="utf-8")
        print(f"Đã lưu file đã xử lý: {output_path}")
    
    except Exception as e:
        print(f"Lỗi khi xử lý file: {e}")

