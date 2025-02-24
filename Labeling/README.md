# **README - Labeling Module**

## **Giới thiệu**
Module **Labeling** chịu trách nhiệm gán nhãn cảm xúc (tích cực, tiêu cực) cho dữ liệu văn bản đã được thu thập và làm sạch. Quá trình này sử dụng mô hình **Sentiment Analysis** để tự động đánh giá cảm xúc của từng câu và lưu kết quả vào tệp CSV để sử dụng trong các bước tiếp theo.

## **Cấu trúc module**
```
Labeling/
├── config.py                 # Cấu hình mô hình, đường dẫn dữ liệu và nhãn
├── main.py                   # Script chính để chạy quá trình gán nhãn
├── preprocessing.py          # Tiền xử lý dữ liệu trước khi gán nhãn
├── chunk_data.py             # Chia dữ liệu thành các phần nhỏ để xử lý
├── label_by_model.py         # Gán nhãn bằng mô hình sentiment analysis
├── merge_processed_chunks.py # Hợp nhất dữ liệu sau khi gán nhãn

Data/
└── Labeling/                 # Thư mục chứa dữ liệu đầu ra
```

## **Cách cài đặt**
### 1. Cài đặt môi trường
Đảm bảo bạn đã cài đặt Python (>=3.7) và các thư viện cần thiết:
```sh
pip install pandas numpy transformers datasets tqdm
```

## **Hướng dẫn sử dụng**
### 1. Tiền xử lý dữ liệu
Chạy lệnh sau để làm sạch dữ liệu trước khi gán nhãn:
```sh
cd Labeling
python preprocessing.py
```
Dữ liệu đầu ra sẽ được lưu tại thư mục `/Data/Labeling/preprocessing.csv`.

### 2. Chia dữ liệu thành các phần nhỏ
Để tối ưu hóa việc xử lý, dữ liệu sẽ được chia thành nhiều phần nhỏ:
```sh
python chunk_data.py
```
Các tệp **chunk_1.csv**, **chunk_2.csv**, ... sẽ được lưu trong thư mục `/Data/Labeling/chunk_input/`.

### 3. Gán nhãn tự động bằng mô hình AI
Chạy lệnh sau để gán nhãn cảm xúc:
```sh
python label_by_model.py
```
Quá trình này sẽ sử dụng mô hình `5CD-AI/Vietnamese-Sentiment-visobert` để phân tích cảm xúc của từng câu.

### 4. Hợp nhất dữ liệu đã gán nhãn
Sau khi tất cả các phần dữ liệu đã được gán nhãn, chạy lệnh sau để hợp nhất:
```sh
python merge_processed_chunks.py
```
Kết quả cuối cùng sẽ được lưu vào `/Data/Labeling/label.csv`.

## **Kết quả đầu ra**
- **`preprocessing.csv`**: Dữ liệu sau khi tiền xử lý.
- **`chunk_x.csv`**: Các tệp dữ liệu đã chia nhỏ để gán nhãn.
- **`label.csv`**: Dữ liệu cuối cùng sau khi gán nhãn.

## **Mô tả chi tiết từng module**
### **1. `preprocessing.py`**
- Kiểm tra dữ liệu đầu vào.
- Loại bỏ dữ liệu trùng lặp và rỗng.
- Lưu kết quả tiền xử lý vào tệp CSV.

### **2. `chunk_data.py`**
- Chia dữ liệu thành nhiều phần nhỏ để tối ưu hiệu suất xử lý.
- Lưu các tệp chia nhỏ vào thư mục `/Data/Labeling/chunk_input/`.

### **3. `label_by_model.py`**
- Sử dụng mô hình sentiment analysis (`5CD-AI/Vietnamese-Sentiment-visobert`) để gán nhãn.
- Dữ liệu được gán nhãn sẽ lưu vào thư mục `/Data/Labeling/chunk_output/`.

### **4. `merge_processed_chunks.py`**
- Gộp tất cả các tệp đã gán nhãn thành một tệp duy nhất `label.csv`.
- Xóa các tệp nhỏ sau khi hợp nhất.
