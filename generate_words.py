import random 
from string import ascii_lowercase as alphabet

def save_word(word):
    with open('word_list.json','a') as f:
        f.write(word + ' ') 


def generate_words():
    for i in range(100):
        wl = random.randrange(1,10)
        wrd = ''
        for x in range(wl):
            wrd += random.choice(alphabet)
        print(wrd) 
        save_word(wrd)

if __name__ == "__main__":
    generate_words()
        




