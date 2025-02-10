
def main():
    book_directory = "books/frankenstein.txt"
    book_text = open_book(book_directory)
    book_word_count = word_count(book_text)
    print (book_text)
    print (f"Word count: {book_word_count}")


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

main()