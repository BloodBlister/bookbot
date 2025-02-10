
def main():
    book_directory = "books/frankenstein.txt"
    book_text = open_book(book_directory)
    lowercase_book_text = book_text.lower()
    book_character_count = character_count(lowercase_book_text)
    book_word_count = word_count(book_text)
    print (f"Summary Report for book: {book_directory}:")
    print (f"Word count: {book_word_count}")
    for character in book_character_count:
        if character.isalpha():
            count = book_character_count[character]
            print (f"Character: '{character}' found {count} times")


def open_book(directory):
    with open(directory) as f:
        file_contents = f.read()
    return (file_contents)

def word_count(text):
    split_words = text.split()
    num_words = 0
    for word in split_words:
        num_words += 1
    return (num_words)

def character_count(text):
    character_dictionary = {}
    for character in text:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    return character_dictionary

main()