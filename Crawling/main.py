from product_scraper import get_product_ids
from comment_scraper import crawl_comments
from utils import get_categories

if __name__ == "__main__":
    # print("Đang lấy danh sách ngành hàng từ API...")
    # categories = get_categories()
    
    # if not categories:
    #     print("Không lấy được danh mục, dừng chương trình.")
    #     exit()

    # print("📌 Bắt đầu crawl danh sách sản phẩm...")
    # for category_name, category_id in categories.items():
    #     print(f"\n➡️ Crawl sản phẩm cho danh mục: {category_name} (ID: {category_id})")
    #     get_product_ids(category_name, category_id)

    print("\nBắt đầu crawl bình luận...")
    crawl_comments()

    print("\nHoàn thành!")
