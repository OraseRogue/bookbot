def count_words(book):
    words = book.split()
    return len(words)

def count_letters(book):
    letters = {}
    book_lower = book.lower()
    for letter in book_lower:
        if letter in letters and letter.isalpha():
            letters[letter] = letters[letter] + 1
        elif letter.isalpha():
            letters[letter] = 1
    return letters_sort(letters)

def letters_sort(letters_dict):
    letters_list = []
    for letter in letters_dict:
        tmp_letter = (letter, letters_dict[letter])
        letters_list.append(tmp_letter)
    letters_list.sort(key=lambda tup: tup[1], reverse=True)
    return letters_list