import os

CLEANING_FOLDER = r"../Data/cleaning/"

INPUT_FILE_PATH = r"../Data/crawling/comments_data.csv"
REMOVE_URL_EMOJI_OUTPUT_PATH = CLEANING_FOLDER + r"remove_url_emoj/remove_url_emoj.csv"
CHUNKING_BEFORE_MODEL_FILE_PATH = CLEANING_FOLDER + r"chunk_input/"
CHUNKING_AFTER_MODEL_FILE_PATH = CLEANING_FOLDER + r"chunk_output/"
OUTPUT_FILE_PATH = CLEANING_FOLDER + r"output/"
OUTPUT_MERGED_FILE_NAME = r"output_merged_model.csv"
OUTPUT_REMOVE_PUNCTUATION_FILE_NAME = r"output_remove_punctuation.csv"
OUTPUT_CLEANING_FILE_NAME = r"cleaning.csv"

COLUMN_NAME_TO_CLEAN= "content"
COLUMN_NAME_AFTER_CLEAN = "clean_content"

PATTERN_OUTPUT_FILE_NAME = "chunk_*.csv"
CHUNK_SIZE = 100 #Số lượng file được chia

# Mô hình sửa lỗi
MODEL_NAME = "bmd1905/vietnamese-correction"
MODEL_TYPE = "text2text-generation"
MAX_LENGTH = 512
BATCH_SIZE = 96