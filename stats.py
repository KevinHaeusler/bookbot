import string

def get_num_words(text):
    #print(f"Found {len(text.split())} total words")
    return len(text.split())

def get_num_char(text):
    char_dict = dict()
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    #print(char_dict)
    return char_dict

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list