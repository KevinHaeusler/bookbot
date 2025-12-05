from stats import get_num_words, get_num_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    get_num_words(get_book_text("books/frankenstein.txt"))
    get_num_char(get_book_text("books/frankenstein.txt"))

main()