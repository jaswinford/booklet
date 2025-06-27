from gc import freeze
from stats import get_charcount_sorted, get_wordcount
from stats import get_charcount

def get_book_text(filepath):
    output = None
    with open(filepath) as f:
        output = f.read()
    return output


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

    frankenstein = get_book_text("books/frankenstein.txt")
    frankenstein_wordcount = get_wordcount(frankenstein)
    print(f"Found {frankenstein_wordcount} total words")

    print("--------- Character Count -------")
    charcount = get_charcount_sorted(frankenstein)
    for char, count in charcount:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()
