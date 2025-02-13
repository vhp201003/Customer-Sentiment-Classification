from preprocessing import preprocessing
from chunk_data import chunk_data
from label_by_model import label_by_model
from merge_processed_chunks import merge_processed_chunks

from config import INPUT_FILE_PATH, \
                    PREPROCESSING_OUTPUT_FOLDER, \
                    PREPROCESSING_OUTPUT_FILE_NAME, \
                    CHUNKING_BEFORE_MODEL_FILE_PATH, \
                    CHUNKING_AFTER_MODEL_FILE_PATH, \
                    LABELS, \
                    OUTPUT_FILE_PATH, \
                    OUTPUT_MERGED_FILE_NAME

def main():
    # preprocessing(INPUT_FILE_PATH, 
    #             PREPROCESSING_OUTPUT_FOLDER,
    #             PREPROCESSING_OUTPUT_FILE_NAME)
    
    # chunk_data(PREPROCESSING_OUTPUT_FOLDER + PREPROCESSING_OUTPUT_FILE_NAME,  
    #         CHUNKING_BEFORE_MODEL_FILE_PATH)

    # label_by_model(CHUNKING_BEFORE_MODEL_FILE_PATH, 
    #                 CHUNKING_AFTER_MODEL_FILE_PATH, 
    #                 LABELS)

    merge_processed_chunks(CHUNKING_AFTER_MODEL_FILE_PATH, 
                            OUTPUT_FILE_PATH, 
                            OUTPUT_MERGED_FILE_NAME)

if __name__ == '__main__':
    main()