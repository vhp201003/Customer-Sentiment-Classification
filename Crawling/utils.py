import os
import pandas as pd
from config import HEADERS, CATEGORY_API
import requests

def save_to_csv(data, file_name):
    """
    Lưu danh sách dữ liệu vào file CSV.
    """
    df = pd.DataFrame(data)
    file_exists = os.path.exists(file_name)
    df.to_csv(file_name, mode='a', header=not file_exists, index=False)

def parse_comment(json, product_name):
    """
    Xử lý dữ liệu bình luận từ JSON.
    """
    try:
        return {
            'id': json.get('id', 'null'),
            'title': json.get('title', 'null'),
            'content': json.get('content', 'null').replace('\n', ' ').replace('\r', ' ') if json.get('content') else 'null',
            'customer_id': json.get('customer_id', 'null'),
            'rating': json.get('rating', 'null'),
            'customer_name': json.get('created_by', {}).get('name', 'null'),
            'product_name': product_name,
            'product_id': json.get('product_id', 'null')
        }
    except Exception as e:
        print(f"Error parsing comment: {e}")
        return None

def get_categories():
    """
    Gửi request đến API và trích xuất danh sách danh mục sản phẩm.
    
    Returns:
        dict: Dictionary chứa tên danh mục và category ID.
    """
    try:
        response = requests.get(CATEGORY_API, headers=HEADERS)
        if response.status_code == 200:
            # Lấy dữ liệu từ trường menu_block.items
            menu_block = response.json().get('menu_block', {})
            items = menu_block.get('items', [])
            
            # Trích xuất tên danh mục (text) và category ID từ link
            category_dict = {}
            for item in items:
                category_name = item.get('text')  # Tên danh mục
                link = item.get('link')  # Link chứa category ID
                if category_name and link:
                    # Lấy category ID từ link
                    category_id = link.split('/c')[-1]
                    category_dict[category_name] = category_id
            
            return category_dict
        else:
            print(f"❌ Lỗi khi lấy danh mục: {response.status_code}")
            return {}
    except Exception as e:
        print(f"❌ Lỗi trong quá trình lấy danh mục: {e}")
        return {}