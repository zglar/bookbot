def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_of_words = len(book_text.split())
    print(f"{num_of_words} words found in the document")

main()