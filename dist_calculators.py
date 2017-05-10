__author__ = "Adrian 'LucidCharts' Campos, Johnson Nguyen, Josh Hicken"
from string import punctuation as punc_chars # this is a string of punctuation chars from python standard lib
from collections import OrderedDict

# noinspection SpellCheckingInspection
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def get_frequency_dist_characters(input_string):
    """
    Calculate frequency of each character's occurrence
    :param input_string: String containing characters to be counted
    :return: A dictionary of characters with their values
    """
    # Set up blank dictionary to store occurrences of each character
    character_dist = {}

    # Iterate through each letter in alphabet and count occurrences in mString
    for letter in ALPHABET:
        # Store number of occurrences in dictionary
        character_dist[letter] = input_string.lower().count(letter)

        # Clean up dictionary; if this letter doesn't exist in mString, remove it
        if character_dist[letter] == 0:
            del character_dist[letter]

    return character_dist


def get_frequency_dist_words_top10(input_string):
    """
    Calculate frequency of top ten words occurring in a phrase
    :param input_string: String containing words to be ranked and limited to 10
    :return: A dictionary of words with their values (length 10)
    """
    # generate the full distribution by stripping bad chars, splitting into tokens, lowering then counting
    phrase = input_string.replace('\r', '').replace('\n', '')
    for char in punc_chars:
        phrase = phrase.replace(char, ' ')
    normalized_tokens = [token.lower() for token in phrase.split(' ')]
    unique_tokens = list(set(normalized_tokens))
    freq_dist = {word:normalized_tokens.count(word) for word in unique_tokens if word != ''}

    # now sort so we can get top 10 items in distribution
    ordered_dist = OrderedDict(sorted(freq_dist.items(), key=lambda x: x[1], reverse=True))

    # trim to top ten. alas, the sort is lost after this, but the worthiness of the items lives on
    freq_dist = {pair[0]: pair[1] for pair in list(ordered_dist.items())[:10]}

    return freq_dist


def get_frequency_dist_first_letters(input_string):
    """
    Calculate frequency of first letter of each word's occurrence
    :param input_string: String containing words whose first letters are to be counted
    :return: A dictionary of characters with their values
    """
    text = input_string.upper()
    text = " " + text
    chararacterFrequency_FirstLetter = {}

    for i in range(len(text)):
        if text[i] == " ":
            if (text[i + 1] not in chararacterFrequency_FirstLetter.keys()) and (text[i + 1] not in punc_chars):
                chararacterFrequency_FirstLetter[text[i + 1]] = 0

            # Characters like '-' will throw a KeyError.
            # We don't care about them, so let's sloppily ignore anything that gives us trouble.
            try:
                chararacterFrequency_FirstLetter[text[i + 1]] += 1
            except KeyError:
                pass

    return chararacterFrequency_FirstLetter
