from stats import word_counter, character_appear, chars_dict_to_sorted_list
import sys

book_path = sys.argv[1]


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["character"].isalpha():
            continue
        print(f"{item['character']}: {item['num']}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return 1
    contents = get_book_text(book_path)
    num_words = word_counter(contents)
    char_dict = character_appear(contents)
    sorted_list = chars_dict_to_sorted_list(char_dict)
    print_report(book_path, num_words, sorted_list)


main()
