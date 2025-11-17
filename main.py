from stats import get_num_words, get_symbol_count, analyze_text
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    # print(f"Found {num_words} total words")

    symbols = get_symbol_count(text)
    # print(symbols)

    analysis = analyze_text(symbols)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in analysis:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")



main()