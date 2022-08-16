from curses.ascii import isalpha
from pickle import APPEND
import random
from secrets import choice
from turtle import clear

class Gassman():

    def __init__(self, num_lives=int, word='', word_guessed=[], num_letters=int, list_letters=[]):
        self.num_lives = num_lives
        self.word = word
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.list_letters = list_letters

   
    def get_word(self):
        self.num_lives=6
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        return

    def ask_letter(self): 
        self.visual_rep()
        print(self.word_guessed)
        letter = input(f'please enter one letter: ')
        letter = letter.lower()
        if letter.isalpha() == False or len(letter)!=1:
            print("try again, this is an incorrect input please only one letter: ")
            self.ask_letter()
        elif letter in self.list_letters:
            print(f'{letter} has already been tried, try again')
            self.ask_letter() 
        else:
            self.list_letters.append(letter)
            self.check_letter()
        
        
    def save_letter(self):
        for position, char in enumerate(self.word):
            if char == self.list_letters[-1]:
                self.word_guessed[position] = self.list_letters[-1] 

    def check_letter(self):
        if self.list_letters[-1] in self.word :
            print(f'well done {self.list_letters[-1]} is in the word')
            self.save_letter()
            #self.ask_letter()
            self.life_counter()
            
        else:
            print('try again, that letter was not in the word')
            lives = self.num_lives-1
            self.num_lives = lives
            print(f'you now have {lives} left')
            #self.ask_letter()
            self.life_counter()
            
        pass
       
    def life_counter(self):
        if self.word_guessed == list(self.word):
            print(f'well done you guessed correctly, the word is:\n{list(self.word)}')
        elif self.num_lives == 0:
            self.visual_rep()
            print(f'Game over, better luck next time, the word was {self.word}')
        else:
            self.ask_letter()   

    def visual_rep(self):
        if self.num_lives == 6:
            print('----------')
            print('|        |') 
            print('|        ') 
            print('|       ') 
            print('|       ')
        elif self.num_lives == 5:
            print('----------')
            print('|        |') 
            print('|        O') 
            print('|       ') 
            print('|       ')
        elif self.num_lives == 4:
            print('----------')
            print('|        |') 
            print('|        O') 
            print('|        |') 
            print('|       ')
        elif self.num_lives == 3:
            print('----------')
            print('|        |') 
            print('|        O') 
            print('|       -|') 
            print('|       ')
        elif self.num_lives == 2:
            print('----------')
            print('|        |') 
            print('|        O') 
            print('|       -|-') 
            print('|       ')
        elif self.num_lives == 1:
            print('----------')
            print('|        |') 
            print('|        O') 
            print('|       -|-') 
            print('|       / ')
        else:
            self.num_lives == 0
            print('----------')
            print('|        |') 
            print('|        O') 
            print('|       -|-') 
            print('|       / \x5c')    

            




def play_game(word_list):
    game = Gassman(word_list)
    game.get_word()
    print('Welcome to Hangman!!\n\nPlease try guess the word below')
    print(f'you have {game.num_lives} lives\n')
    game.ask_letter()

        
        
    

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
        




    


    
        


