import requests
import time
import random
import csv
from config import HEADERS, PRODUCT_PARAMS, PRODUCT_API, DATA_DIR
import os


def get_product_ids(category_name, category_id, output_file="product_id.csv"):
    """
    Crawl danh sách ID sản phẩm từ một danh mục cụ thể trên Tiki và lưu vào CSV.

    Args:
        category_name (str): Tên danh mục sản phẩm (VD: "Điện Gia Dụng").
        category_id (str): ID của danh mục sản phẩm (VD: "1882").
        output_file (str, optional): Đường dẫn file CSV lưu dữ liệu. Mặc định lưu trong thư mục DATA_DIR.
    """
    # Nếu không chỉ định file output, tự động tạo file theo category_name
    if output_file is None:
        output_file = os.path.join(DATA_DIR, f"product_{category_name.replace(' ', '_')}.csv")
    else:
        output_file = os.path.join(DATA_DIR, output_file)
        
    # Mở file và ghi header
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['id'])
        writer.writeheader()

    # Cập nhật tham số danh mục cho API
    PRODUCT_PARAMS['category'] = category_id

    # Bắt đầu crawl từ trang đầu tiên
    page = 1
    while True:
        PRODUCT_PARAMS['page'] = page
        try:
            # Gửi request đến API
            response = requests.get(PRODUCT_API, headers=HEADERS, params=PRODUCT_PARAMS)
            response.raise_for_status()  # Kiểm tra lỗi HTTP

            # Lấy danh sách sản phẩm
            data = response.json().get('data', [])
            if not data:  # Dừng nếu không có thêm sản phẩm
                print(f"No more products for category '{category_name}' on page {page}. Stopping.")
                break

            # Ghi ID sản phẩm vào file
            with open(output_file, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['id'])
                for record in data:
                    writer.writerow({'id': record.get('id')})

            print(f"✅ Crawled page {page} of category '{category_name}' successfully.")

        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed for page {page} of category '{category_name}': {e}")
            break

        # Chuyển sang trang tiếp theo
        page += 1
        time.sleep(random.uniform(1, 3))  # Thêm độ trễ để tránh bị chặn