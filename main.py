from stats import count_words
from stats import char_counter
from stats import char_presorter
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:        
        path = sys.argv[1]
        content = get_book_text(path)
        num_words = count_words(content)
        print("============ BOOKBOT ============")
        print(f" Analyzing book found at {path}....")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        characters = char_counter(content)
        char_presorted = char_presorter(characters)
        for element in char_presorted:
            character = element["Character"]
            num = element["num"]
            print(f"{character}: {num}")


main()