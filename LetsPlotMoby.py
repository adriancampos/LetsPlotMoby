import matplotlib.pyplot as plt
import dist_calculators

FILE_MOBY_SMALL = "assets\\mobysmall.txt"
FILE_MOBY_BIG = "assets\\moby.txt"


def main():
    # Characters
    show_graph(dist_calculators.get_frequency_dist_characters(load_from_file(FILE_MOBY_SMALL)),
               title="Character Distribution - Mobysmall", style='bo')

    show_graph(dist_calculators.get_frequency_dist_characters(load_from_file(FILE_MOBY_BIG)),
               title="Character Distribution - Mobysmall", style='bo', sort_mode=1)

    # Top 10 Words
    show_graph(dist_calculators.get_frequency_dist_words_top10(load_from_file(FILE_MOBY_SMALL)),
               sort_mode=1, style='y', linewidth=5, title="Word Distribution - Mobysmall")

    show_graph(dist_calculators.get_frequency_dist_words_top10(load_from_file(FILE_MOBY_BIG)),
               sort_mode=1, style='y', linewidth=5, title="Word Distribution - Moby")

    # First Letters
    show_graph(dist_calculators.get_frequency_dist_first_letters(load_from_file(FILE_MOBY_SMALL)),
               style="r--", title="First Letter Distribution - Mobysmall")

    show_graph(dist_calculators.get_frequency_dist_first_letters(load_from_file(FILE_MOBY_BIG)),
               style="r--", title="First Letter Distribution - Moby")


def load_from_file(filename):
    with open(filename) as file:
        return file.read()


def show_graph(frequency_dict, sort_mode=0, style='b', title="Figure 1", **kwargs):
    """
    Creates graph based on frequency of character/word
    :param frequency_dict: dictionary containing each letter or word and their respective frequency 
    :param style: style to pass to plt.plot()
    :param kwargs: any more keyword args (linewidth, markersize, etc.) to pass to plt.plot()
    :return: 
    """
    # gets a list of tuples containing the letters as the first value and frequency as the second
    # sorts the list to put them in alphabetical order
    if sort_mode == 0:
        freqDictList = sorted(frequency_dict.items())
    else:
        import operator
        freqDictList = sorted(frequency_dict.items(), key=operator.itemgetter(1), reverse=True)

    # creates empty lists to later hold the values of the x value labels and the y values of the graph
    xTicks = []
    yVals = []

    # loops through the list of tuples and appends the x and y values to their appropriate lists
    for tup in freqDictList:
        xTicks.append(tup[0])
        yVals.append(tup[1])

    # creates x vals list to represent the letters on the graph
    xVals = range(len(xTicks))

    # labels the x values with their appropriate names
    plt.xticks(xVals, xTicks)

    plt.title(title)

    # plots the x and y values then displays the graph
    plt.plot(xVals, yVals, style, **kwargs)  # style=style, linewidth=linewidth, markersize=markersize, alpha=alpha)
    plt.show()


main()
