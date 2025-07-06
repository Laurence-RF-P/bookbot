import sys
from stats import get_num_words, get_symbol_count, get_sorted_list

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]
book_text = get_book_text(filepath=file_path)
word_count = get_num_words(book_text=book_text)
symbol_count = get_symbol_count(book_text=book_text)
char_list = get_sorted_list(char_dict=symbol_count)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in char_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")

main()