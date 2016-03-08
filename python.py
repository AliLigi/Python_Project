#find 9 letter anagram

# timer function to see how long it takes to run this program
import time
start_time = time.time()

with open('wordList.txt', 'r') as fileopen:
	words= [line.strip() for line in fileopen]

anagram ="test"

#this is an import of permutations that comes up with all permutations of a word.
from itertools import permutations

perms = [''.join(p)for p in permutations(anagram)]

print(set(perms) & set(words))

# prints out to the console the running time of the program
print("--- %s seconds ---" % (time.time() - start_time))