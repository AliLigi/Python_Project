# timer function to see how long it takes to run this program
import time
start_time = time.time()

#Get all the words from the file, and form a set using set comprehension
with open('wordList.txt', 'r') as fileopen:
	words= [line.strip() for line in fileopen]
	
# Importing random, then set vowels and consonants
import random
anagram = []
vowels = ['a','e','i','o','u']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','w','y']

# 3 loops that allow you to choose 3 vowels , 4 constants and 2 random vowels or consonant
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

#prints the longest word it finds in the list of words
print (sortWord[-1])

# prints out to the console the running time of the program
print("--- %s seconds ---" % (time.time() - start_time))