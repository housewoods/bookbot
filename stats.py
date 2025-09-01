def count_words(string):
    num_words = len(string.split())
    return num_words

def char_counter(string):
    characters_dict = {}
    string = string.lower()
    for char in string:
        if char in characters_dict.keys():
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    return characters_dict

def sort_on(items):
    return items["num"]

def char_presorter(char_dict):
    char_presorted_list = []
    i = 0
    keys = char_dict.keys()
    for key in char_dict:
        if key.isalpha() == True:
            key_dict = {
                "Character" : key, "num" : char_dict[key]
            }
            char_presorted_list.append(key_dict)

    char_presorted_list.sort(reverse=True, key = sort_on)
    return char_presorted_list
    


