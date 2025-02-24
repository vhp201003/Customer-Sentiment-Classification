# Customer-Sentiment-Classification

## Giới thiệu
Dự án này nhằm thu thập, làm sạch và phân tích cảm xúc trên văn bản tự động. Quy trình gồm các bước chính sau:
1. **Crawling** - Thu thập dữ liệu bình luận từ các trang web.
2. **Cleaning** - Tiền xử lý và chuẩn hóa dữ liệu.
3. **Labeling** - Gán nhãn cảm xúc tự động bằng AI.

Dữ liệu sau khi xử lý sẽ được sử dụng trong các bước tiếp theo như huấn luyện mô hình và phân tích xu hướng.

---

## Cấu trúc dự án
```
Dự án
├── Crawling/      # Module thu thập dữ liệu
├── Cleaning/      # Module làm sạch dữ liệu
├── Labeling/      # Module gán nhãn cảm xúc
├── Data/          # Lưu trữ dữ liệu đầu ra
├── README.md      # Tài liệu hướng dẫn
```

---

## Hướng dẫn cài đặt
### 1. Cài đặt môi trường
Hãy cài đặt các thư viện cần thiết:
```sh
pip install requests pandas tqdm numpy transformers datasets emoji num2words
```

---

## Hướng dẫn sử dụng
### **1. Thu thập dữ liệu (Crawling)**
```sh
cd Crawling
python main.py
```
- **`product_scraper.py`**: Thu thập danh sách ID sản phẩm.
- **`comment_scraper.py`**: Thu thập bình luận từ các ID sản phẩm.

### **2. Tiền xử lý dữ liệu (Cleaning)**
```sh
cd Cleaning
python main.py
```
- **Xóa URL, emoji, ký tự dư thừa.**
- **Sửa lỗi chính tả.**
- **Loại bỏ dữ liệu trùng lặp.**

### **3. Gán nhãn tự động (Labeling)**
```sh
cd Labeling
python main.py
```
- **Sử dụng mô hình `5CD-AI/Vietnamese-Sentiment-visobert`.**
- **Phân loại cảm xúc: "Tích cực" - "Tiêu cực".**

---

## Kết quả đầu ra
- **`comments_data.csv`**: Dữ liệu bình luận thu thập từ API.
- **`cleaning.csv`**: Dữ liệu đã được làm sạch.
- **`label.csv`**: Dữ liệu đã gán nhãn cảm xúc.

---

## Lưu ý
- **API crawling** có thể thay đổi, cần kiểm tra `config.py` khi gặp lỗi.
- **Xử lý chính tả** tôn nhiều tài nguyên, nên chạy tất cả các file chunk trước khi gộp.
- **Gán nhãn AI** có thể chạy lâu, hãy chia nhỏ dữ liệu trước khi gán nhãn.

---