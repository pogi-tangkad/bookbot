def get_num_words(text):
    word_count = 0
    for word in text.split():
        word_count += 1
    return word_count



def sort_characters(text):
    char_dict = {}
    for char in text:
        if char.lower() not in char_dict:
            char_dict[char.lower()] = 1
        else:
            char_dict[char.lower()] += 1
    return char_dict