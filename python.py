#Alina Danci 
#G00302444@gmit.ie

#find 9 letter anagram
# word list/ word list --https://github.com/dwyl/english-words

# timer function to see how long it takes to run this program
import time
start_time = time.time()

#Get all the words from the file, and form a set using set comprehension
with open('wordlist.txt', 'r') as fileopen:
	words= [line.strip() for line in fileopen]

#Converting to words lowerCase	
words = [item.lower() for item in words]
#============================================================================================================	
#from itertools import permutations
#with open('wordlist.txt') as f:
#   words = {line.rstrip('\n').lower() for line in f}
#  for potential_word  in map(''.join, permutations('aeiourst')):
#     if potential_word  in words:
#      print(potential_word)
#============================================================================================================		
# Importing random, then set vowels and consonants
import random
anagram = []
vowels = ['a','e','i','o','u']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','w','y']
	
#anagram ="python"

#=============================================================================================================
#a different way of genetating a random algorithm 
# randomly creating a shuffled word
#def genRandomAlgo():
#	anagram = []
#	for i in range(0, 9):
#		if i < 3:
#			anagram += random.choice(vowels)
#			if i > 3 & i < 7:
#				anagram += random.choice(consonants)
#				if i > 7:
#					anagram += random.choice(vowels + consonants)
#	return anagram 
#=============================================================================================================

# 3 loops that allow you to choose 3 vowels , 4 constants and 2 random vowels or consonant
# randomly generates a suffle of 3 vowels , 4 constants and 2 random vowels or consonant and then it solves it, it finds all the possible words and then sorts the word and gives the largest word found.

for i in range (0,3):
    anagram.append(random.choice(vowels))
for i in range (0,4):
    anagram.append(random.choice(consonant))
for i in range (0,2):
    anagram.append(random.choice(vowels + consonant))

#Importing the shuffle function, which shuffles the anagram/letters that were chosen above  
from random import shuffle
shuffle(anagram)

# this prints the anagram on the screen but and does not allow for , to appear in the shuffled words
print (''.join(anagram))

# This imports the the itertools function permutations which sets out the counter and then lists all the permutations
# —itertools.permutations()—takes a collection of items and produces a sequence of tuples that rearranges all of the 
#items into all possible permutations (i.e., it shuffles them into all possible configurations)

from itertools import permutations
j = 0
permutation = []

#======================================================================================================================
# another  way to generate the permutations
#def permutations(letters):
#   letters = list(letters)
#    if len(letters) == 1:
#       yield letters
#    for letter in set(letters):
#        letters.remove(letter)
#        for perm in perms(letters):
#            yield [letter] + perm
#        letters.append(letter)
#Genetating all possible permutations of a word 
#def genPerms(word):
#    allPermuts = []
    
#    for i in range(1, 10):
#        allPermuts += permutations(word, i)
           
#    return allPermuts
#========================================================================================================================

# This looops 9 times because this is the max we will always have
# Finding all possible permutations of a given string
# Join permuted letters /words
for i in range (0,9):
    permutation += [''.join(p) for p in permutations(anagram, j)]
    j += 1
#perms = [''.join(p)for p in permutations(anagram)]

#words and permutation convert to sets which allow only unique list
res = (set(words) & set(permutation))

#orders the words and give the largest word it finds
sortWord = sorted(res, key=len)

#first prints out the word that is set as the anagram
print(anagram)

#then this prints out all the permutations 
print(set(words) & set(permutation))

#prints the longest word it finds in the list of words
print (sortWord[-1])

# prints out to the console the running time of the program
print("--- %s seconds ---" % (time.time() - start_time))