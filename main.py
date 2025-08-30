def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def count_words(string):
    num_words = len(string.split())
    return num_words

def main():
    content = get_book_text("books/frankenstein.txt")
    num_words = count_words(content)
    print(f"{num_words} words found in the document")



main()