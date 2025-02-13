
import pandas as pd
import numpy as np
import os
from config import CHUNK_SIZE

# Chia dữ liệu và lưu vào ./input
def save_chunks_to_input_chunk(df, n_chunks, input_folder):
    # Kiểm tra nếu thư mục ./input đã có file
    if os.listdir(input_folder):
        print(f"Directory {input_folder} already contains files. Skipping chunk creation.")
        return

    # Chia và lưu chunk
    for idx, chunk in enumerate(np.array_split(df, n_chunks)):  # Sử dụng np.array_split để chia DataFrame
        chunk_file = os.path.join(input_folder, f"chunk_{idx + 1}.csv")
        chunk.to_csv(chunk_file, index=False, encoding="utf-8")
        print(f"Chunk {idx + 1} saved to {chunk_file}")

def chunk_data(input_path, output_path):
    os.makedirs(output_path, exist_ok=True)
    processed_df = pd.read_csv(input_path)
    save_chunks_to_input_chunk(processed_df, CHUNK_SIZE, output_path)
