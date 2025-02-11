import pandas as pd
from num2words import num2words
import os
import re
import string

def replace_numbers(text):
    # Thay thế các số thành các chuỗi với các ký tự đặc biệt như chấm, dấu phẩy, dấu chấm, dấu cách, dấu chấm của tiếng Việt.
    text = re.sub(r'\d+', lambda x: num2words(int(x.group()), lang='vi'), text)
    return text

# def remove_punctuation(text):
#     # Xóa các ký tự đặc biệt như chấm, dấu phẩy, dấu chấm, dấu cách, dấu chấm của tiếng Việt.
#     text = text.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
#     return text

def remove_punctuation(text):
    # Tạo bảng dịch thay thế dấu câu bằng khoảng trắng
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    text = text.translate(translator)
    # Xóa khoảng trắng thừa nếu có
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_punctuation_and_replace_numbers(input_folder, output_folder, input_name_file, output_name_file, column_to_process):
    """
    - Đọc các file chunk trong input_folder và lấy các dữ liệu từ các file.
    - Xóa các ký tự đặc biệt như chấm, dấu phẩy, dấu chấm, dấu cách, dấu chấm của tiếng Việt.
    - Thay thế các số thành các chuỗi với các ký tự đặc biệt như chấm, dấu phẩy, dấu chấm, dấu cách, dấu chấm của tiếng Việt.
    - Lưu file đã xử lý vào output_folder.
    - Xóa file gốc sau khi đã xử lý.
    - Hiển thị thanh tiến trình và log thông tin số chunk đang xử lý.
    """
    # Đảm bảo thư mục output tồn tại
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df = pd.read_csv(input_folder + input_name_file)
    df[column_to_process] = df[column_to_process].apply(lambda x: remove_punctuation(x) if isinstance(x, str) else "")
    df[column_to_process] = df[column_to_process].apply(lambda x: replace_numbers(x) if isinstance(x, str) else "")
    df.to_csv(output_folder + output_name_file, index=False, encoding="utf-8")
    print(f"Đã xóa ký tự đặc biệt như chấm, dấu phẩy, dấu chấm, dấu cách, dấu chấm của tiếng Việt.")
    print(f"Đã thay thế các số thành các chuỗi với các ký tự đặc biệt như chấm, dấu phẩy, dấu chấm, dấu cách, dấu chấm của tiếng Việt.")
    print(f"Đã lưu file đã xử lý vào {output_folder}.")
    print(f"Đã xóa file gốc sau khi đã xử lý.")