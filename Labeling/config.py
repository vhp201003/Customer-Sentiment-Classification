import os

LABEL_FOLDER = r"../Data/labeling/"

INPUT_FILE_PATH = r"../Data/cleaning/output/cleaning.csv"
PREPROCESSING_OUTPUT_FOLDER = LABEL_FOLDER + r"preprocessing/"
PREPROCESSING_OUTPUT_FILE_NAME = r"preprocessing.csv"

CHUNKING_BEFORE_MODEL_FILE_PATH = LABEL_FOLDER + r"chunk_input/"
CHUNKING_AFTER_MODEL_FILE_PATH = LABEL_FOLDER + r"chunk_output/"

OUTPUT_FILE_PATH = LABEL_FOLDER + r"output/"
OUTPUT_MERGED_FILE_NAME = r"label.csv"

COLUMN_NAME_TO_LABEL= "clean_content"
COLUMN_NAME_LABEL = "label"
LABELS = ["tích cực", "tiêu cực"]

PATTERN_OUTPUT_FILE_NAME = "chunk_*.csv"
CHUNK_SIZE = 100 #Số lượng file được chia
# Mô hình sửa lỗi
MODEL_NAME = "joeddav/xlm-roberta-large-xnli"
MODEL_TYPE = "zero-shot-classification"
MAX_LENGTH = 512
BATCH_SIZE = 96