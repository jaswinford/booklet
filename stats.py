def get_wordcount(body):
    words = body.split()
    return len(words)

def get_charcount(body):
    body = body.lower()
    output = {}
    for char in body:
        output[char] = output.get(char, 0) + 1
    return output

def get_charcount_sorted(body):
    charcount = get_charcount(body)
    sorted_chars = sorted(charcount.items(), key=lambda x: x[1], reverse=True)
    return sorted_chars
