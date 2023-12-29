import random
from hungman_words import *
from hangman_art import *

if __name__ == '__main__':
    result =  random.choice(word_list)
    print(result)
    s = '_'*len(result)
    life = 6
    print(logo)
    
    while(True):
        x = input('Guess a word: ')
        if x in result:
            if x in s:
                print('You have already guess the same')
                continue
            for i in range(0,len(result)):
                if result[i] == x:
                    string_list = list(s)
                    string_list[i] = result[i]
                    s = "".join(string_list)
                    print(s)
                    print(stages[life])
        else:
            life -= 1
            print(s)
            print('You Guesed Wrong')
            print(stages[life])
        if life == 0:
            print('You Lost the game')
            break
        elif '_' not in s:
            print('You Won the game')
            break
                
    
    print(s)