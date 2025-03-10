def count_words(text):
    return len(text.split())

def count_character_num(text):
    characters = {}
    for char in text:
        if char.lower() not in characters:
            characters[char.lower()] = 1
        else:
            characters[char.lower()] += 1
    return characters

def sort_on(dict):
    return dict["Num"]

def sort_chars(chars):
    char_list = []
    for char in chars:
        char_list.append({"Character": char, "Num": chars[char]})
    char_list.sort(key=sort_on, reverse=True)
    return char_list
    