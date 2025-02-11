import pandas as pd
import numpy as np
from multiprocessing import Pool, cpu_count
import re
import emoji

from config import COLUMN_NAME_TO_CLEAN, \
                    COLUMN_NAME_AFTER_CLEAN

def remove_emojis(text):
    # Loại bỏ emoji Unicode
    text = ''.join(char for char in text if char not in emoji.EMOJI_DATA)
    # Loại bỏ ký tự mặt cười (smilies) và các chuỗi lặp liên tiếp
    smiley_pattern = r'(:\)+|:\(+|:D+|:P+|:O+|:o+|:3+|<3+|;\)+|;-P+|:-\)+|:-\(+|:-D+|\)+|\(+)'
    text = re.sub(smiley_pattern, '', text)
    # Loại bỏ khoảng trắng thừa sau khi xóa smilies
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def process_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)  # Xóa URL
    text = remove_emojis(text)  # Xóa emoji
    text = re.sub(r'\s+', ' ', text).strip()  # Loại bỏ khoảng trắng thừa
    return text

def process_dataframe_chunk(chunk):
    #Detect language
    # chunk = chunk[chunk[COLUMN_NAME_TO_CLEAN].apply(lambda x: detect_language(x, target="vi"))].copy()
    ###
    chunk.loc[:, COLUMN_NAME_AFTER_CLEAN] = chunk[COLUMN_NAME_TO_CLEAN].apply(lambda x: process_text(x) if isinstance(x, str) else "")
    return chunk

def parallel_process_dataframe(df, n_processes=None):
    if n_processes is None:
        n_processes = cpu_count()  # Số lượng CPU hiện tại
    df_split = np.array_split(df, n_processes)  # Chia nhỏ DataFrame
    with Pool(n_processes) as pool:
        processed_chunks = pool.map(process_dataframe_chunk, df_split)  # Xử lý từng phần
    return pd.concat(processed_chunks)  # Gộp lại

def remove_url_emoji(input_path, output_path):
    df = pd.read_csv(input_path)
    processed_df = parallel_process_dataframe(df)
    processed_df.dropna(inplace=True)
    processed_df.drop_duplicates(inplace=True)
    processed_df.reset_index(drop=True, inplace=True)
    processed_df.to_csv(output_path, index=False)
