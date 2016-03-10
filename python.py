#find 9 letter anagram

# timer function to see how long it takes to run this program
import time
start_time = time.time()

#Get all the words from the file, and form a set using set comprehension
with open('wordList.txt', 'r') as fileopen:
	words= [line.strip() for line in fileopen]
#from itertools import permutations
#with open('wordlist.txt') as f:
 #   words = {line.rstrip('\n').lower() for line in f}
 #  for potential_word  in map(''.join, permutations('aeiourst')):
 #     if potential_word  in words:
 #      print(potential_word)
			
	
anagram ="python"

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


#first prints out the word that is set as the anagram
print(anagram)
#then this prints out the permutations 
print(set(words) & set(permutation))
# prints out to the console the running time of the program
print("--- %s seconds ---" % (time.time() - start_time))