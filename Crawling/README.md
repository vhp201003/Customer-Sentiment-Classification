# **Giới thiệu**

Module này chịu trách nhiệm thu thập dữ liệu sản phẩm và bình luận từ Tiki.vn thông qua API của họ. Dữ liệu thu thập sẽ được lưu vào thư mục /Data/crawling để sử dụng trong các bước tiếp theo như làm sạch dữ liệu, gán nhãn và huấn luyện mô hình.

# **Cấu trúc module**

Crawling/
├── config.py              # Cấu hình API và các tham số mặc định
├── main.py                # Script chính để chạy quá trình crawling
├── product_scraper.py     # Thu thập danh sách sản phẩm
├── comment_scraper.py     # Thu thập bình luận của sản phẩm
├── utils.py               # Các hàm tiện ích
└── Data/crawling/         # Thư mục chứa dữ liệu CSV đầu ra

**Cách cài đặt**

Đảm bảo bạn đã cài đặt Python (>=3.7) và các thư viện cần thiết:

pip install requests pandas tqdm

**Hướng dẫn sử dụng**

### **1. Thu thập danh sách sản phẩm**

Chạy lệnh sau để lấy danh sách sản phẩm theo danh mục:

cd Crawling
python main.py

Script main.py sẽ gọi product_scraper.py để lấy danh sách sản phẩm và lưu vào product_id.csv.

### **2. Thu thập bình luận sản phẩm**

Sau khi có danh sách sản phẩm, chạy tiếp để thu thập bình luận:

python main.py

Script sẽ sử dụng comment_scraper.py để lấy dữ liệu bình luận từ API và lưu vào comments_data.csv.

Kết quả đầu ra

product_id.csv: Chứa danh sách ID sản phẩm

comments_data.csv: Chứa dữ liệu bình luận của sản phẩm

**Mô tả chi tiết từng module**

### **1. product_scraper.py**

Crawl danh sách sản phẩm theo danh mục.

Lưu ID sản phẩm vào CSV.

Gửi request đến API Tiki với các tham số phù hợp.

### **2. comment_scraper.py**

Duyệt qua từng sản phẩm và lấy bình luận.

Lưu bình luận vào CSV.

Tự động dừng khi không còn dữ liệu.

### **3. utils.py**

Chứa các hàm hỗ trợ như lưu dữ liệu vào CSV, parse bình luận.

**Lưu ý**

API có thể thay đổi theo thời gian, nếu có lỗi cần kiểm tra lại URL API trong config.py.

Một số request có thể bị chặn nếu gửi quá nhiều trong thời gian ngắn. Có thể chỉnh thời gian delay trong product_scraper.py.
