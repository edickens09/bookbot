def main():
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        print(count_words(file_contents))


def count_words(book):
    word_count = 0
    count = book.split()
    for word in count:
        word_count += 1
    return word_count
    

main()