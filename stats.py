def word_counter(text):
    content = text.split()
    return len(content)


def character_appear(text):
    content = text.lower()
    chars = {}
    for c in content:
        if c not in chars:
            chars[c] = 0
    for key in chars:
        counter = 0
        for c in content:
            if key == c:
                counter += 1
            chars[key] = counter
    return chars


def sort_on(dict):
    return dict["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"character": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
