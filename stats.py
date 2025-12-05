import string

char_dict = dict()

def get_num_words(text):
    print(f"Found {len(text.split())} total words")
    return len(text.split())

def get_num_char(text):
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    print(char_dict)