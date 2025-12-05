def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    print(f"Found {len(text.split())} total words")
    return len(text.split())

def main():
    count_words(get_book_text("books/frankenstein.txt"))

main()