
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    #print(word_count(text))
    #print(char_count(text))
    return report_printing(text, book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    
    return counter

def char_count(text):
    lowered_text = text.lower()
    joined = "".join(lowered_text)
    alpha_list = []
    alpha_dict = {}

    for textchar in joined:
        if textchar.isalpha():
            if textchar not in alpha_list:
                alpha_list.append(textchar)
    
    for letter in alpha_list:
        letter_count = joined.count(letter)
        alpha_dict.update({f"{letter}": letter_count})
        letter_count = 0

    return alpha_dict

def report_printing(text, book_path):
    wordcount = word_count(text)
    charactercount = char_count(text)
    path = book_path

    print(f"-- Begin Report of {path} ---")
    print(f"{wordcount} words found in this document")
    
    for k in charactercount:
        print(f"The '{k}' character was found {charactercount[k]} times.")
    
    print("--- End Report ---")
    
main()