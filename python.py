#find 9 letter anagram
#lists

with open('wordList.txt', 'r') as fileopen:
	words= [line.strip() for line in fileopen]

anagram ="test"

from itertools import permutations
perms = [''.join(p)for p in permutations(anagram)]

print(set(perms) & set(words))