def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_text(book_path)

    num_of_words = get_number_of_words(book_text)
    character_dict = sort_characters(book_text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_of_words} words foind in the book.")
    print()
    for char in character_dict:
        if 97 <= ord(char) <= 122:
            print(f"The '{char}' character was found {character_dict[char]} times.")

    print("--- End report ---")





def sort_characters(text):
    char_dict = {}
    for char in text:
        if char.lower() not in char_dict:
            char_dict[char.lower()] = 1
        else:
            char_dict[char.lower()] += 1
    return char_dict



def get_number_of_words(text):
    word_count = 0
    for word in text.split():
        word_count += 1
    return word_count




def get_text(book):
    with open(book) as f:
        return f.read()



if __name__ == "__main__":
    main()
