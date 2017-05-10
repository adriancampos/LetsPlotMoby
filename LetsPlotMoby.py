import matplotlib.pyplot as plt
import dist_calculators

FILE_MOBY_SMALL = "assets\\mobysmall.txt"
FILE_MOBY_BIG = "assets\\moby.txt"


def main():
    # Characters
    show_graph(dist_calculators.get_frequency_dist_characters(load_from_file(FILE_MOBY_SMALL)),
        style='r--', linewidth=10, markersize=15)  # TODO Style this a little better

    show_graph(dist_calculators.get_frequency_dist_characters(load_from_file(FILE_MOBY_BIG)),
               title="Bigger File")

    # Top 10 Words
    show_graph(dist_calculators.get_frequency_dist_words_top10(load_from_file(FILE_MOBY_SMALL)),
        linewidth=1)

    show_graph(dist_calculators.get_frequency_dist_words_top10(load_from_file(FILE_MOBY_BIG)),
               title="Josh, this one takes forever")

    # First Letters
    show_graph(dist_calculators.get_frequency_dist_first_letters(load_from_file(FILE_MOBY_BIG)),
               )

    show_graph(dist_calculators.get_frequency_dist_first_letters(load_from_file(FILE_MOBY_SMALL)),
               )


def load_from_file(filename):
    with open(filename) as file:
        return file.read()


def show_graph(frequency_dict, style='b', title="Figure 1", **kwargs):
    """
    Creates graph based on frequency of character/word
    :param frequency_dict: dictionary containing each letter or word and their respective frequency 
    :param style: style to pass to plt.plot()
    :param kwargs: any more keyword args (linewidth, markersize, etc.) to pass to plt.plot()
    :return: 
    """
    #gets a list of tuples containing the letters as the first value and frequency as the second
    #sorts the list to put them in alphabetical order
    freqDictList = sorted(frequency_dict.items())
    
    #creates empty lists to later hold the values of the x value labels and the y values of the graph
    xTicks = []
    yVals = []

    #loops through the list of tuples and appends the x and y values to their appropriate lists
    for tup in freqDictList:
        xTicks.append(tup[0])
        yVals.append(tup[1])

    #creates x vals list to represent the letters on the graph
    xVals = range(len(xTicks)) 

    #labels the x values with their appropriate names
    plt.xticks(xVals, xTicks)

    plt.title(title)
    
    #plots the x and y values then displays the graph
    plt.plot(xVals, yVals, style, **kwargs)# style=style, linewidth=linewidth, markersize=markersize, alpha=alpha)
    plt.show()

main()