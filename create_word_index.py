# PLAN
# create script to generate 1000 words DONE
# create txt file to save words DONE
# write code to do indexing DONE
# write interface to search for words DONE
# write tests to automatically search for words

# Return where in the list the word appears 
# create L words in order 
# when index created, place L idx @ end under key=idx/location
# in search, when confirmed True, return idx



import pdb 
from typing import List
from copy import deepcopy
                
with open('word_list.json','r') as f:
    words = f.read()
words = 'the blue black cat car in the city city city takes the time to take her home'
words = 'be back soon'
print('WORDS_STR: ', words)
lst_words = words.split()

def create_list_word_chars(words:str) -> List[List]:
    words_split_set = set(words.split())
    words_split_list = sorted([word for word in words_split_set])
    # print('WORD SPLIT LIST ', words_split_list)
    words_char_split = []
    for w in words_split_list: # List[List], word chars
        char_word_list = [char for char in w]
        words_char_split.append(char_word_list)
    return words_char_split

# create index
def sort(words_char_split:List[List],lst_words:List[str]) -> dict: 
    index = {}
    current_index = index

    for word in words_char_split:
        word_str = ""
        for l in word:
            word_str += l
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
        # pdb.set_trace()
        current_index['idx'] = lst_words.index(word_str)
        current_index = index
    return index
    
full_index = sort(create_list_word_chars(words), lst_words)
print(full_index)


def find_word(index_dict:dict) -> bool:
    word = input('search index for word: ')
    copy_index_dict = deepcopy(index_dict)
    for i in range(len(word)):
        if word[i] in index_dict.keys():
            index_dict = index_dict[word[i]]
        else:
            print(False)  
            search_again = input('search another word? y/n ')
            if search_again[0].lower() == 'n':
                return False
            else:
                find_word(copy_index_dict)         
    try:
        print("Word in index at location: " + str(index_dict['idx']))
    except KeyError:
        print(False)

    search_again = input('search another word? y/n ')
    if search_again[0].lower() == 'n':
        return 
    else:
        find_word(copy_index_dict)


if __name__ == '__main__':
    find_word(full_index)





