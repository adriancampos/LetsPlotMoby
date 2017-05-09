from string import punctuation as punc_chars # this is a string of punctuation chars from python standard lib

def get_word_frequency_dist(phrase):
    # TODO determine proper order of stripping punctuation and stripping newlines, + correct replacement char for punc
    phrase = phrase.replace('\r', ' ').replace('\n', ' ')
    for char in punc_chars:
        phrase = phrase.replace(char, ' ')

    tokenized_phrase = phrase.split(' ')
    normalized_phrase = [token.lower() for token in tokenized_phrase]
    unique_tokens = list(set(normalized_phrase))
    return {word:normalized_phrase.count(word) for word in unique_tokens}
