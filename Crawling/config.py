HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
    'Accept': 'application/json, text/plain, */*',
}

# API lấy danh mục sản phẩm
CATEGORY_API = "https://api.tiki.vn/raiden/v2/menu-config?platform=desktop"

# API lấy danh sách sản phẩm
PRODUCT_API = "https://tiki.vn/api/personalish/v1/blocks/listings"

# API lấy thông tin chi tiết sản phẩm
PRODUCT_INFO_API = "https://tiki.vn/api/v2/products/"

# API lấy bình luận sản phẩm
COMMENT_API = "https://tiki.vn/api/v2/reviews"

# Các tham số mặc định cho việc crawl sản phẩm
PRODUCT_PARAMS = {
    'limit': '40',  # Số sản phẩm mỗi trang
    'page': '1',    # Trang hiện tại
}

# Các tham số mặc định cho việc crawl bình luận
COMMENT_PARAMS = {
    'product_id': '',           # ID sản phẩm
    'sort': 'score|desc,id|desc,stars|all',  # Tiêu chí sắp xếp
    'page': '1',                # Trang hiện tại
    'limit': '10',              # Số bình luận mỗi trang
    'include': 'comments,contribute_info',  # Các trường dữ liệu bổ sung
}

DATA_DIR = r"../Data/crawling"