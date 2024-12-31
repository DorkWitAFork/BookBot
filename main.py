def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
        
    final_report(file_contents)
    
def word_count(contents):
    return len(contents.split())

def char_counter(contents):
    chars = contents.lower()
    chars_dict = {}
    for char in chars:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def final_report(contents):
    words = word_count(contents)
    chars_count = char_counter(contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")
    
    for char in chars_count:
        print(f"The {char} character was found {chars_count[char]} times")
    
    print("\n--- End report ---")


main()