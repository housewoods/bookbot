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
