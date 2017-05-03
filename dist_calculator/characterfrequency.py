# noinspection SpellCheckingInspection
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def get_character_frequency_dist(input_string):
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
