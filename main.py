import sys
from stats import get_num_words
from stats import get_num_characters

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    words_count = get_num_words(filepath)
    char_count = get_num_characters(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for ch, cnt in char_count.items():
        print(f"{ch}: {cnt}")
    print("============= END ===============")

main()