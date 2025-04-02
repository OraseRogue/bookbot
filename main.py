from stats import count_words
from stats import count_letters


def main():
    source = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {source}...")
    with open(source) as f:
        file_contents = f.read()
        no_words = count_words(file_contents)
        no_letters = count_letters(file_contents)
        print_report(no_words, no_letters)
        return 0

def print_report(word_count, letters):
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter_list in letters:
        print(f"{letter_list[0]}: {letter_list[1]}")
    print("============= END ===============")
    return 0


main()