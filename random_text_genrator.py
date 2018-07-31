#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 12:54:31 2018

@author: ajay yadav
"""

import random  # for gentrating random things may be random letter or number
import string  # for genrating the string

vowels ='aeiou' # for vowels
consonants = 'bcdfghjklmnpqrstvwxy' # for consonants
letter = string.ascii_lowercase # to apply lowercase letters 
list1 = ['v','c', 'l'] # list containg the valid items to be selected for particular word
# for taking the choice for random word to genrate
letter_input_1  = input("Select your choice. Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
while(letter_input_1 not in list1): # conditions for taking only valid input
    letter_input_1 =input("Please fill the valid choice, Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")

letter_input_2  = input("Select your choice. Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
while(letter_input_2 not in list1):
    letter_input_2 =input("Please fill the valid choice, Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
    
letter_input_3  = input("Select your choice. Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
while(letter_input_3 not in list1):
    letter_input_3 =input("Please fill the valid choice, Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
    
letter_input_4  = input("Select your choice. Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
while(letter_input_4 not in list1):
    letter_input_4 =input("Please fill the valid choice, Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
    
letter_input_5  = input("Select your choice. Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
while(letter_input_5 not in list1):
    letter_input_5 =input("Please fill the valid choice, Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
    
letter_input_6  = input("Select your choice. Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
while(letter_input_6 not in list1):
    letter_input_6 =input("Please fill the valid choice, Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
# to print the choice of letter you have entered
print(letter_input_1+letter_input_2+letter_input_3+letter_input_4+letter_input_5+letter_input_6)

def genrate(): # function which genrate random letter
    if letter_input_1 == 'v' :
       letter1 = random.choice(vowels)
    elif letter_input_1 == 'c' :
       letter1 = random.choice(consonants)
    else :
       letter1 = random.choice(letter)
    
    
    if letter_input_2 == 'v' :
       letter2 = random.choice(vowels)
    elif letter_input_2 == 'c' :
       letter2 = random.choice(consonants)
    else :
       letter2 = random.choice(letter)
    
    
    if letter_input_3 == 'v' :
       letter3 = random.choice(vowels)
    elif letter_input_3 == 'c' :
       letter3 = random.choice(consonants)
    else :
       letter3 = random.choice(letter)
    
     
    if letter_input_4 == 'v' :
       letter4 = random.choice(vowels)
    elif letter_input_4 == 'c' :
       letter4 = random.choice(consonants)
    else :
       letter4 = random.choice(letter)

    if letter_input_5 == 'v' :
       letter5 = random.choice(vowels)
    elif letter_input_5 == 'c' :
       letter5 = random.choice(consonants)
    else :
       letter5 = random.choice(letter)
       
    if letter_input_6 == 'v' :
       letter6 = random.choice(vowels)
    elif letter_input_6 == 'c' :
       letter6 = random.choice(consonants)
    else :
       letter6 = random.choice(letter)


    # formation of words after taking value from conditon and genrator
    word = letter1 +letter2 +letter3 +letter4 +letter5 +letter6
    return word
# for printing value more than one time
no_of_words_to_be_genrated = input("Enter the no. of words you want to genrate:")
for i in range(int(no_of_words_to_be_genrated)):
    print(genrate())

