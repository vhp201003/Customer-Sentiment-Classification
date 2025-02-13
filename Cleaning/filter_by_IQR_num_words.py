import pandas as pd
import os

def word_length(word):
    return len(word)

def filter_by_IQR_num_words(input_folder, output_folder, input_name_file, output_name_file, column_to_process):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df = pd.read_csv(os.path.join(input_folder, input_name_file))

    df["word_count"] = df[column_to_process].apply(lambda x: len(str(x).split()))

    Q1 = df["word_count"].quantile(0.25)
    Q3 = df["word_count"].quantile(0.75)
    IQR = Q3 - Q1

    df_filtered = df[(df["word_count"] >= Q1) & (df["word_count"] <= Q3)]
    df_filtered = df_filtered.drop(columns=["word_count"])
    df_filtered.to_csv(output_folder + output_name_file, index=False, encoding="utf-8")
