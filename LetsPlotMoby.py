import matplotlib.pyplot as plt

def show_graph(frequency_dict):
    """
    Creates graph based on frequency of character/word
    parameter is a dictionary containing each letter or word and their respective frequency
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
    
    #plots the x and y values then displays the graph
    plt.plot(xVals, yVals)
    plt.show()
