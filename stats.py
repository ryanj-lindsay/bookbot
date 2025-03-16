def get_num_words(string_book):
    num_words = string_book.split()
    return len(num_words)

def get_num_chars(book_path):
    char_dict = {}
    for i in book_path:
        i = i.lower()
        if i not in char_dict:
            char_dict.update({i : 1})
        else:
            char_dict[i] += 1
    return char_dict



def sort_char_dict(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_data = {'char': char, 'num': count}
        char_list.append(char_data)
        
    def sort_on(dict_value):
        return dict_value['num']
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list