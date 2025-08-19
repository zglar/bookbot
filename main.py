from stats import get_num_words
from stats import get_num_characters
from stats import char_count_report

def main():
    filepath = "books/frankenstein.txt"
    words_count = get_num_words()
    char_count = char_count_report()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for ch, cnt in char_count.items():
        print(f"{ch}: {cnt}")
    print("============= END ===============")

main()