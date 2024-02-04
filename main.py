def main():
    book_path = "books/Frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        #print(file_contents)
        #print(count_words(file_contents))
        #print(count_letters(file_contents))
        #print(generate_report(file_contents))
        print_report(file_contents, book_path)

def count_words(book):
    word_count = 0
    count = book.split()
    for word in count:
        word_count += 1
    return word_count

def count_letters(book):
    letter_dict = {}
    lower_string = book.lower()
    string_split = lower_string.split()

    for word in string_split:
        for letter in word:
        
            if letter in letter_dict:
                letter_dict[letter] += 1

            else:
                letter_dict[letter] = 1

    return letter_dict

def sort_on(dict):
    return dict["Count"]

def generate_report(book):
    letter_dict = count_letters(book)
    remove_dict = []
    letter_list = []

    #Generating a list of items not letters to later remove from letter_dict because wouldn't let me delete directly in for loop
    for check in letter_dict:
        if check.isalpha() == False:
            remove_dict.append(check)
    for remove in remove_dict:
        del letter_dict[remove]

    for letter, num in letter_dict.items():
        letter_list.append({"Letter":letter, "Count":num})

    letter_list.sort(key= sort_on, reverse= True)
    
    return letter_list

def print_report (book, book_path):
    print(f"--- Begin report of" , book_path, "---")
    print(count_words(book), "words found in the document")
    letter_count = generate_report(book)
    for dictionary in letter_count:
        letter = dictionary["Letter"]
        count = dictionary["Count"]
        print(f"The",letter, "character was found",count,"times")
    print("--- End report ---")
main()