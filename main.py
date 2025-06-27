import sys
from stats import get_charcount_sorted, get_wordcount

def get_book_text(filepath):
    output = None
    with open(filepath) as f:
        output = f.read()
    return output

def print_report(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")

    body = get_book_text(filepath)
    wordcount = get_wordcount(body)
    print(f"Found {wordcount} total words")

    print("--------- Character Count -------")
    charcount = get_charcount_sorted(body)
    for char, count in charcount:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print_report(filepath)

main()
