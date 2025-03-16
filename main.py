from stats import get_num_words, get_num_chars, sort_char_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    num_words = get_num_words(get_book_text(file_path))
    num_chars = get_num_chars(get_book_text(file_path))
    sorted_num_chars = sort_char_dict(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("============ Word Count ============")
    print(f"Found {num_words} total words")
    print("============ Character Count ============")
    for sub_dicts in sorted_num_chars:
        if sub_dicts['char'].isalpha() == True:
            print(f"{sub_dicts['char']}: {sub_dicts['num']}")
    print('============ END ============')
    
if __name__ == '__main__':
    main()