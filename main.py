book_name = "frankenstein.txt"
book_location = "books/"+book_name

def open_book():
    with open(book_location) as f:
        file_contents = f.read()
        words = file_contents.split()
        #print(words)
        total_words = count_words(words)
        #print(total_words)
        word_dict = count_characters(words)
        word_dict_sorted = sorted(word_dict.items(),key=lambda x:x[1], reverse=True)
        final_dict = dict(word_dict_sorted)
        #print(word_dict_sorted)
        print(f"--- Begin Report of books/{book_name} ---")
        print(f"{total_words} words found in the document")
        for name, value in final_dict.items():
             if name.isalpha():
                print(f"The {name} character was found {value} times")
        print("-- End Report ---")
     

def count_words(file_to_read):
        count = 0
        for word in file_to_read:
            count += 1
        return count

def count_characters(string_to_read):
    character_tally = {}
    lowered_string = string_to_read
    for word in lowered_string:
        for letter in word.lower():
            if letter not in character_tally:
                character_tally[letter] = 1
            else:
                 character_tally[letter] += 1
    return character_tally

def sorted_on(dict):
     return dict.values()

def main():
        open_book()


main()