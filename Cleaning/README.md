# README - Cleaning Module

## Giới thiệu
Module này chịu trách nhiệm làm sạch dữ liệu review sản phẩm trước khi đưa vào quá trình phân tích cảm xúc. Các bước chính bao gồm:
- Xóa URL và emoji
- Chia dữ liệu thành các phần nhỏ (chunking)
- Sửa lỗi chính tả
- Gộp dữ liệu sau khi xử lý
- Xóa dấu câu và thay thế số bằng chữ

Dữ liệu được lưu trữ tại thư mục `/Data/cleaning` để phục vụ cho các bước tiếp theo.

## Cấu trúc module
```
Cleaning/
├── config.py                                  # Cấu hình đường dẫn và tham số
├── main.py                                    # Script chính để chạy toàn bộ quá trình cleaning
├── remove_url_emoj.py                         # Xóa URL và emoji khỏi dữ liệu
├── chunk_data.py                              # Chia dữ liệu thành các phần nhỏ
├── spelling_correction.py                     # Sửa lỗi chính tả bằng mô hình pre-trained
├── merge_processed_chunks.py                  # Gộp dữ liệu sau khi xử lý
├── remove_punctuation_and_replace_numbers.py  # Xóa dấu câu và thay thế số bằng chữ
├── filter_by_IQR_num_words.py                 # Lọc ra các từ quá ngắn hoặc quá dài 

Data/
└── cleaning/                            # Thư mục chứa dữ liệu đã làm sạch
```

## Cách cài đặt
### 1. Cài đặt môi trường
Đảm bảo bạn đã cài đặt Python (>=3.7) và các thư viện cần thiết:
```sh
pip install pandas numpy tqdm emoji transformers datasets num2words
```

## Hướng dẫn sử dụng
### 1. Chạy quá trình làm sạch dữ liệu
Thực thi lệnh sau để chạy toàn bộ pipeline cleaning:
```sh
cd Cleaning
python main.py
```
Script `main.py` sẽ gọi lần lượt các module xử lý dữ liệu theo đúng thứ tự.

## Kết quả đầu ra
- `remove_url_emoj.csv`: Dữ liệu sau khi xóa URL và emoji
- `chunk_input/`: Dữ liệu đã chia nhỏ trước khi đưa vào mô hình
- `chunk_output/`: Dữ liệu đã qua sửa lỗi chính tả
- `output_merged_model.csv`: Dữ liệu đã gộp lại sau khi sửa lỗi chính tả
- `output_remove_punctuation.csv`: Dữ liệu đã loại bỏ dấu câu và thay thế số bằng chữ
- `cleaning.csv`: Dữ liệu đã lọc ra các từ quá ngắn hoặc quá dài

## Mô tả chi tiết từng module
### 1. `remove_url_emoj.py`
- Xóa URL, emoji, ký tự mặt cười (smiley) khỏi dữ liệu review.
- Loại bỏ khoảng trắng thừa sau khi xử lý.

### 2. `chunk_data.py`
- Chia dữ liệu review thành nhiều phần nhỏ để xử lý hiệu quả hơn.
- Lưu từng phần vào thư mục `chunk_input/`.

### 3. `spelling_correction.py`
- Sửa lỗi chính tả bằng mô hình pre-trained (`bmd1905/vietnamese-correction`).
- Áp dụng batch processing để tăng tốc độ xử lý.

### 4. `merge_processed_chunks.py`
- Gộp lại các file chunk sau khi sửa lỗi chính tả.
- Xóa các file chunk gốc sau khi gộp dữ liệu.

### 5. `remove_punctuation_and_replace_numbers.py`
- Xóa dấu câu khỏi dữ liệu.
- Chuyển đổi số thành chữ để giữ nguyên ý nghĩa của câu.

### 6. `filter_by_IQR_num_words.py`
- Lọc ra các từ quá ngắn hoặc quá dài

## Lưu ý
- Các file đầu vào và đầu ra được quy định trong `config.py`, bạn có thể thay đổi đường dẫn nếu cần.
- Một số quá trình xử lý có thể mất thời gian, đặc biệt là sửa lỗi chính tả.
- Nếu gặp lỗi thiếu thư viện, hãy kiểm tra lại các thư viện đã cài đặt.
