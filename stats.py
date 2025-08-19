def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(filepath):
    book_text = get_book_text(filepath)
    return len(book_text.split())

def get_num_characters(filepath):
    char_counts = {}
 
    book_text = get_book_text(filepath).lower().split()
    for word in book_text:
        for char in word:
            if char.isalpha():
                char_counts[char] = char_counts.get(char,0) + 1
    
    sorted_char = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_char

