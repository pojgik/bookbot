from stats import get_word_count, count_characters, sort_chars
import sys

def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
    return book_contents

def main():
    if (len(sys.argv) != 2):
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    word_count = get_word_count(book)
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    sorted_list = sort_chars(count_characters(book))
    for d in sorted_list:
        if d['char'].isalpha():
            print(f"{d['char']}: {d['num']}")
    print('============= END ===============')
main()