def get_book_text(filepath):
    output = None
    with open(filepath) as f:
        output = f.read()
    return output

def get_wordcount(body):
    words = body.split()
    return len(words)

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    frankenstein_wordcount = get_wordcount(frankenstein)
    print(f"{frankenstein_wordcount} words found in the document")

main()
