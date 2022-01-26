# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 15:36:58 2022

@author: Nima
"""


def search_for_vowels(phrase: str) -> set:
    """Search for vowels in entered word"""
    v = set('aeiou')
    found = v.intersection(set(phrase))
    return found


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """(Letters) Found In (Phrase), Letters Default Is Vowels"""
    return set(letters).intersection(set(phrase))
