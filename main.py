import sys
from stats import (
    get_num_words, 
    get_char_dict, 
    sort_dict,
)



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    char_dict = get_char_dict(text)
    sorted_dict = sort_dict(char_dict)
    print_report(book_path, word_count, sorted_dict)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()    

def print_report(book_path, word_count, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")


main()