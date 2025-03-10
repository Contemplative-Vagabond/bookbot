import sys
from stats import count_words, count_character_num, sort_chars

def get_book_text(file_path):
    text = ""
    with open(file_path) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py book/file/path.txt")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    word_count = count_words(text)
    char_count = count_character_num(text)
    sorted_chars = sort_chars(char_count)

    #setup for printing formated report
    #Header;
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    #loop for printing character count;
    for char in sorted_chars:
        string = char["Character"]
        num = char["Num"]
        if string.isalpha():
            print(f"{string}: {num}")
        else:
            continue


    #END
    print("============= END ===============")

main()