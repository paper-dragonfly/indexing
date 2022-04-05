# PLAN
# create script to generate 1000 words DONE
# create txt file to save words DONE
# write code to do indexing 
# write interface to search for words
# write tests to automatically search for words

import pdb 
from typing import List
                
with open('word_list.json','r') as f:
    words = f.read()
words = 'the blue black cat car in the city city city takes the time to take her home'

def create_list_word_chars(words:str) -> List[List]:
    words_split_set = set(words.split())
    words_split_list = sorted([word for word in words_split_set])
    print('WORD SPLIT LIST ', words_split_list)
    words_char_split = []
    for w in words_split_list: # List[List], word chars
        char_word_list = [char for char in w]
        words_char_split.append(char_word_list)
    return words_char_split


def sort(words_char_split:List[List]): 
    index = {}
    current_index = index

    for word in words_char_split:
        while len(word) > 0: 
            char = word.pop(0) 
            if char in current_index.keys(): 
                # pdb.set_trace()
                unique = False
                while unique == False:
                    current_index = current_index[char] 
                    char = word.pop(0)
                    if char in current_index.keys(): 
                        continue
                    else:
                        unique = True 

            next_level = {} 
            current_index[char] = next_level
            current_index = next_level
        current_index = index
    return index
    
full_index = sort(create_list_word_chars(words))


def find_word() -> bool:
    word = input('search if a word is in the index: ')
    pdb.set_trace
    search_dict = full_index
    for i in range(len(word)):
        if word[i] in search_dict.keys():
            search_dict = search_dict[word[i]]
        else:
            print(False)
            again = input('search again? y/n ')
            if again.lower == 'n':
                return False
            else:
                find_word()
    print(True)
    again = input('search again? y/n ')
    if again.lower == 'n':
        return True 
    else:
        find_word()


if __name__ == '__main__':
    find_word()





