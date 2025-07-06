def get_num_words(book_text: str) -> int:
    word_count = len(book_text.split())
    #print(f"{word_count} words found in the document")
    return word_count

def get_symbol_count(book_text: str) -> dict[str, int]:
    symbol_count = {}
    for char in book_text.lower():
        if char not in symbol_count:
            symbol_count[char] = 1
        else:
            symbol_count[char] += 1
    return symbol_count


def sort_on(items):
    return items["num"]

def get_sorted_list(char_dict: dict[str, int]):
    dict_list = []
    for key, value in char_dict.items():
        dict_list.append({
            "char": key,
            "num": value
        })
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list