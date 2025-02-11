from remove_url_emoj import remove_url_emoji
from chunk_data import chunk_data
from spelling_correction import spelling_correction
from merge_processed_chunks import merge_processed_chunks
from remove_punctuation_and_replace_numbers import remove_punctuation_and_replace_numbers

from config import INPUT_FILE_PATH, \
                    REMOVE_URL_EMOJI_OUTPUT_PATH, \
                    CHUNKING_BEFORE_MODEL_FILE_PATH, \
                    CHUNKING_AFTER_MODEL_FILE_PATH, \
                    OUTPUT_FILE_PATH, \
                    OUTPUT_MERGED_FILE_NAME, \
                    PATTERN_OUTPUT_FILE_NAME, \
                    OUTPUT_REMOVE_PUNCTUATION_FILE_NAME, \
                    COLUMN_NAME_AFTER_CLEAN


def main():
    remove_url_emoji(INPUT_FILE_PATH, 
                    REMOVE_URL_EMOJI_OUTPUT_PATH)
    
    chunk_data(REMOVE_URL_EMOJI_OUTPUT_PATH, 
            CHUNKING_BEFORE_MODEL_FILE_PATH)
    
    spelling_correction(CHUNKING_BEFORE_MODEL_FILE_PATH, 
                    CHUNKING_AFTER_MODEL_FILE_PATH)
    
    merge_processed_chunks(CHUNKING_AFTER_MODEL_FILE_PATH, 
                        OUTPUT_FILE_PATH, 
                        OUTPUT_MERGED_FILE_NAME, 
                        PATTERN_OUTPUT_FILE_NAME)

    remove_punctuation_and_replace_numbers(OUTPUT_FILE_PATH, # Input folder
                                    OUTPUT_FILE_PATH, # Output folder
                                    OUTPUT_MERGED_FILE_NAME, # Input file name
                                    OUTPUT_REMOVE_PUNCTUATION_FILE_NAME, # Output file name
                                    COLUMN_NAME_AFTER_CLEAN) # Column to process

if __name__ == '__main__':
    main()