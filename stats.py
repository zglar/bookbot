def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    return len(book_text.split())