def main():

    #Get File
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    #Count number of words in the text
    number_of_words = word_count(text)
    print(f"Number of words: {number_of_words}")

    #Count the number of characters in the text
    number_of_characters = character_count(text)
    print(f"Number of characters: {number_of_characters}")

    #Introduce the report
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document", end="\n\n")

    #Generate the report
    create_report(number_of_characters)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(book_text):
    list_of_words = book_text.split()
    total_words = len(list_of_words)
    return total_words

def character_count(book_text):
    lowered_text = book_text.lower()
    text_dict = {}
    for i in lowered_text:
        if i in text_dict:
            text_dict[i] += 1
        elif i.isalpha():
            text_dict[i] = 1
        else:
            pass
    total_sum = sum(text_dict.values())
    return text_dict

def create_report(dict):
    sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}
    for key, value in sorted_dict.items():
        print(f"The {key} character was found {value} times")


main()