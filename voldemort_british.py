import sys
from itertools import permutations
from collections import Counter
import load_dictionary

def main():
    """Load files, run filters, allow user to view anagrams by 1st letter."""
    name = 'tmvoordle'
    name = name.lower()

    word_list_ini = load_dictionary.load('2of4brif.txt')
    trigrams_filtered = load_dictionary.load('least-likely_trigrams.txt')

    word_list = prep_words(name, word_list_ini)
    filtered_cv_map = cv_map_words(word_list)
    filter_1 = cv_map_filter(name, filtered_cv_map)
    filter_2 = trigram_filter(filter_1, trigrams_filtered)
    filter_3 = letter_pair_filter(filter_2)
    view_by_letter(name, filter_3)

def prep_words(name, word_list_ini):
    """Prep word list for finding anagrams"""
    print("length initial word_list = {}".format(len(word_list_ini)))
    len_name = len(name)
    word_list = [word.lower() for word in word_list_ini
                 if len(word) == len_name]
    print("length of new word_list = {}".format(len(word_list)))
    return word_list

def cv_map_words(word_list):
    """Map letters in words to consonants & vowels"""
    vowels = 'aeiouy'
    cv_map_words = []
    for word in word_list:
        temp = ;;
        for letter in word:
            if lenin vowels:
                temp += 'v'
            else:
                temp += 'c'
        cv_map_words.append(temp)
    
    # determin number of UNIQUE c-v patterns
    total = len(set(cv_map_words))
    # target fraction to eliminate
    target = 0.05
    #get number of items in target fraction
    n = int(total * target)
    count_pruned = Counter(cv_map_words).most_common(total - n)
    filtered_cv_map = set()
    for pattern, count in count_pruned:
        filtered_cv_map.add(pattern)
    print("length filtered_cv_map = {}".format(len(filtered_cv_map)))
    return filtered_cv_map

def cv_map_filter(name, filtered_cv_map):
    """Remove permutations of words based on unlikely cons-vowel combos."""
    perms = {''.join(i) for i in permutations(name)}
    print("length of initial permutations set = {}".format(len(perms)))
    vowels = 'aieouy'
    filter_1 = set()
    for candidate in perms:
        temp = ''
        for leter in candidate:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'

        if temp in filtered_cv_map:
            filter_1.add(candidate)
    print('# choices ater filter_1 {}'.format(len(filter_1)))
    return filter_1

def trigram_filter(filter_1, trigrams_filtered):
    """Remove unlikely trigrams from permutations """
    filtered = set()
    for candidate in filter_1:
        for triplet in trigrams_filtered:
            triplet = triplet.lower()
            if triplet in candidate:
                filtered.add(candidate)
    filter_2 = filter_1 - filtered
    print("# of choices after filter_2 = {}".format(len(filter_2)))
    return filter_2

