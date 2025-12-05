from stats import get_num_words, get_num_char, chars_dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    get_num_char(get_book_text("books/frankenstein.txt"))
    sorted_list = chars_dict_to_sorted_list(get_num_char(get_book_text("books/frankenstein.txt")))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f" Found {get_num_words(get_book_text("books/frankenstein.txt"))} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")
    print("============= END ===============")
main()