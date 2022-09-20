#Q   Write a function that will find all the anagrams of a word from a list. 
#	 You will be given two inputs a word and an array with words. 
#	 You should return an array of all the anagrams or an empty array if there are none.

#MY SOLUTION
def anagrams(word, words):
	toReturn = []
	str1 = word.lower()
	for s in words:
		str2 = s.lower()
		if (len(str1) == len(str2)):
			sorted_str1 = sorted(str1)
			sorted_str2 = sorted(str2)

			if(sorted_str1 == sorted_str2):
				toReturn.append(s)
	print(toReturn)

anagrams('laser', ['lazing', 'lazy',  'lacer'])

#BEST SOLUTIONS
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]

def anagrams(word, words):
    return filter(lambda x: sorted(word) == sorted(x), words)

from collections import Counter

def anagrams(word, words):
    counts = Counter(word)
    return [w for w in words if Counter(w) == counts]

def anagrams(word, words):
    match = sorted(word)
    return [w for w in words if match == sorted(w)]

