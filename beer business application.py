# -*- coding: utf-8 -*-
"""
Created on Mon May 22 17:36:06 2023

@author: PC
"""

word = "bottles"
for beer_num in range(99,0,-1):
    print(beer_num, word, "of beer on the wall")
    print(beer_num,word, "of beer")
    print("Take one down")
    print("pass it around")
    if beer_num == 1:
        print("No more bottles of beer on the wall")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottles"
            print(new_num, word, " of beer on the wall")
    print()


for i in range (7,0,-2):
    print(i)
    if i == 2:
        print('closer to the endpoint')
    else:
        newi = i - 1
        if newi == 2:
            print('end!')
    print()
    

lst = []
word = "miliways"
vowels = ['a','e', 'i', 'o', 'u']  
for letter in word:
    if letter in vowels:
        print(letter)
        lst.append(letter)
print(lst)
for n in lst:
    if n == n:
        lst.remove(n)
    print(lst) 
    


lst = []
word = "miliways"
vowels = ['a','e', 'i', 'o', 'u'] 
for letter in word:
    if letter in vowels:
        print(letter)
        lst.append(letter)


found = []
vowels = {'a','e', 'i', 'o', 'u'}
for n in range(5):
    word_search = input('please enter a letter to search ')
    for letter in word_search:
        if letter in vowels:
            if letter not in found:
                found.append(letter)

print(found)


lst = [1,2,4]
lst1 = lst.remove(4)
lst1.pop(0)




























    





















    
    
    
            
    
    
    
    
    
    
    
    