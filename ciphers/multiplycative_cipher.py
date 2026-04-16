#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:02:18 2026

@author: kit
"""

letters = "abcdefjhijklmnopqrstuvwxyz"
letter_map = {}
position_map = {}
current_key = 0



word = input("enter the word you wanna encrypt: ").lower()
encryption_key = int(input("enter the encryption key: "))

decrypt_key = [i for i in range(26) if ((encryption_key * i) % 26 == 1)][0]

def create_letter_map(letters):
    count = 0
    for letter in letters:
        letter_map[letter] = count
        position_map[count] = letter
        count += 1
    
def provide_new_key(encryption_key, position):
    new_key = (position * encryption_key) % 26
    return new_key
        
def encrypt_letter(char):
    position = letter_map[char]
    final_key = provide_new_key(encryption_key, position)
    return position_map[final_key]

def encrypt_word(word):
    encrypted_word = ""
    for letter in word:
        encrypted_word += encrypt_letter(letter)
    return encrypted_word



def get_position(char):
    p1 = letter_map[char]
    new_position = ((p1 * decrypt_key) % 26)
    return new_position

def decrypt_letter(char):
    final_key = get_position(char)
    #final_key = provide_new_key(decrypt_key, position)
    return position_map[final_key]


def decrypt_word(word):
    decrypted_word = ""
    for letter in word:
        decrypted_word += decrypt_letter(letter)
    return decrypted_word

create_letter_map(letters)
encrypted_word = encrypt_word(word)

print("encrypted word:", encrypted_word.upper())
print("Decrypted word:", decrypt_word(encrypted_word).upper())
        
    
    
    

    


    