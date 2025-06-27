from stats import get_wordcount

def get_book_text(filepath):
    output = None
    with open(filepath) as f:
        output = f.read()
    return output


def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    frankenstein_wordcount = get_wordcount(frankenstein)
    print(f"{frankenstein_wordcount} words found in the document")

main()
