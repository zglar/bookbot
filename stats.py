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
            if char.isalpha():
                char_counts[char] = char_counts.get(char,0) + 1
    return char_counts

def char_count_report():
    char_count_list = get_num_characters()
    sorted_char = dict(sorted(char_count_list.items(), key=lambda item: item[1], reverse=True))
    return sorted_char
