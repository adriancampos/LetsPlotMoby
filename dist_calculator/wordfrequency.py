from string import punctuation as punc_chars # this is a string of punctuation chars from python standard lib
from collections import OrderedDict


def get_frequency_dist_words_top10(phrase):
    # generate the full distribution by stripping bad chars, splitting into tokens, lowering then counting
    phrase = phrase.replace('\r', '').replace('\n', '')
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
