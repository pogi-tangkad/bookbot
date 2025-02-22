from stats import get_num_words
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python 3 main.py <path_to_book>")
        sys.exit(1)
    book_file = sys.argv[1]
    book_path = book_file
    book_text = get_text(book_path)

    num_of_words = get_num_words(book_text)
    character_dict = sort_characters(book_text)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for char in character_dict:
        if 97 <= ord(char) <= 122:
            print(f"{char}: {character_dict[char]}")

    print("============= END ===============")





def sort_characters(text):
    char_dict = {}
    for char in text:
        if char.lower() not in char_dict:
            char_dict[char.lower()] = 1
        else:
            char_dict[char.lower()] += 1
    return char_dict




def get_text(book):
    with open(book) as f:
        return f.read()



if __name__ == "__main__":
    main()
