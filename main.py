from stats import get_word_count, count_characters

def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
    return book_contents

def main():
    book = get_book_text('books/frankenstein.txt')
    word_count = get_word_count(book)
    print(f'{word_count} words found in the document')
    print(count_characters(book))
main()