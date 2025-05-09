def get_num_words(file):
    list = file.split()
    return len(list)

def get_char_dict(text):
    num_char = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in num_char:
            num_char[char] += 1
        else:
            num_char[char] = 1
    return num_char

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    char_list = []
    for char in dict:
        char_list.append({"char": char, "count":dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list