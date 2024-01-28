def main():
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        print(count_words(file_contents))
        print(count_letters(file_contents))


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
    

main()