import os
import pandas as pd
import fnmatch

def merge_processed_chunks(input_folder, output_folder, output_file_name, pattern="chunk_*.csv"):
    """
    - Đọc các file chunk đã xử lý trong input_folder và merge thành một file CSV.
    - Lưu file CSV được merge vào output_folder.
    - Xóa các file chunk đã xử lý trong input_folder.
    """
    # Đảm bảo thư mục output tồn tại
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lọc các file theo pattern sử dụng fnmatch
    file_list = [file for file in os.listdir(input_folder) if fnmatch.fnmatch(file, pattern)]
    
    # Nếu không có file nào phù hợp, in thông báo và dừng hàm
    if not file_list:
        print("Không có file nào khớp với pattern được chỉ định.")
        return

    # Đọc và nối dữ liệu từ các file CSV
    df = pd.concat([pd.read_csv(os.path.join(input_folder, file)) for file in file_list])
    output_path = os.path.join(output_folder, output_file_name)
    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"Đã lưu file merge tại: {output_path}")

    # Xóa các file chunk đã xử lý
    for file in file_list:
        os.remove(os.path.join(input_folder, file))
        print(f"Đã xóa file: {file}")

if __name__ == "__main__":
    merge_processed_chunks(CHUNKING_AFTER_MODEL_FILE_PATH, OUTPUT_FILE_PATH, OUTPUT_MERGED_FILE_NAME)
