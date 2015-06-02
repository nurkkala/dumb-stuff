#!/usr/bin/env python

english_scrabble_distribution = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12,
    'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1,
    'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8,
    'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6,
    'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2,
    'Z': 1
}

german_scrabble_distribution = {
    'A': 6, 'B': 2, 'C': 2, 'D': 4, 'E': 15,
    'F': 2, 'G': 3, 'H': 4, 'I': 6, 'J': 1,
    'K': 2, 'L': 3, 'M': 4, 'N': 9, 'O': 4,
    'P': 1, 'Q': 1, 'R': 6, 'S': 7, 'T': 6,
    'U': 7, 'V': 1, 'W': 1, 'X': 1, 'Y': 1,
    'Z': 1
}

def possible_word(language, word, distribution):
    possible = True

    for letter in word:
        distribution[letter] -= 1

    for letter in distribution:
        if distribution[letter] < 0:
            possible = False
            print "\tNot enough {}'s ({} too few) in {}".format(letter,
                                                                abs(distribution[letter]),
                                                                language)
    if possible:
        print "\tPlenty of letters in {}".format(language)


word = 'FUSSBODENSCHLEIFMASCHINENVERLEIH'

print "For {}".format(word)
possible_word('English', word, english_scrabble_distribution)
possible_word('German', word, german_scrabble_distribution)
