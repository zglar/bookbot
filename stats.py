def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    return len(book_text.split())

def get_num_characters():
    char_counts = {}
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath).lower().split()
    for word in book_text:
        for char in word:
            char_counts[char] = char_counts.get(char,0) + 1
    return char_counts