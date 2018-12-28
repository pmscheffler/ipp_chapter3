import sys
from collections import Counter
import load_dictionary

dict_file = load_dictionary.load('2of4brif.txt')
# ensure "a" and "I" (both lowercase) are included
dict_file.append('a')
dict_file.append('i')
dict_file = sorted(dict_file)

ini_name = input("Enter a name: ")

def find_anagrams(name, word_list):
    """ Read name & dictionary file & display all anagrams IN name."""
    name_letter_map = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
            if Counter(test) == word_letter_map:
                anagrams.append(word)
    print(*anagrams, sep='\n')
    print()
    print("Remaining letters = {}".format(name))
    print("Number of remaining letters = {}".format(len(name)))
    print("Number of remaining (real world) anagrams = {}".format(len(anagrams)))
    
