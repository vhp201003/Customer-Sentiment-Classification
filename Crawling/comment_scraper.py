import requests
import pandas as pd
from tqdm import tqdm
from config import HEADERS, COMMENT_PARAMS, COMMENT_API, PRODUCT_INFO_API, DATA_DIR
from utils import save_to_csv, parse_comment
import os

def crawl_comments():
    """
    Crawl bình luận cho từng sản phẩm từ file product_id.csv và lưu vào comments_data.csv.
    """
    input_file_path = os.path.join(DATA_DIR, 'product_id.csv')
    output_file_path = os.path.join(DATA_DIR, 'comments_data.csv')

    df_id = pd.read_csv(input_file_path)
    product_ids = df_id['id'].to_list()

    for pid in tqdm(product_ids, total=len(product_ids), desc="Crawling products"):
        COMMENT_PARAMS['product_id'] = pid

        try:
            response_product = requests.get(f"{PRODUCT_INFO_API}{pid}", headers=HEADERS)
            response_product.raise_for_status()
            product_name = response_product.json().get('name', 'Unknown Product')
        except requests.RequestException as e:
            print(f"Error fetching product info for product {pid}: {e}")
            product_name = 'Unknown Product'

        page = 1
        while True:
            COMMENT_PARAMS['page'] = page
            try:
                response = requests.get(COMMENT_API, headers=HEADERS, params=COMMENT_PARAMS)
                response.raise_for_status()
                comments = response.json().get('data', [])

                if not comments:
                    print(f"No more comments found for product {pid} at page {page}.")
                    break

                parsed_comments = [parse_comment(comment, product_name) for comment in comments if comment.get('content')]
                parsed_comments = [c for c in parsed_comments if c is not None]

                save_to_csv(parsed_comments, output_file_path)

                page += 1
            except requests.RequestException as e:
                print(f"Error fetching comments for product {pid} on page {page}: {e}")
                break
