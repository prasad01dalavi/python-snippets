import matplotlib.pyplot as plt
from drawnow import *           # Import all libraries from drawnow
from matplotlib import style

style.use('ggplot')
liveData = []       # Create an empty array to save data from file
plt.ion()           # Turn on interactive mode of matplotlib
cnt = 0             # To see only latest data


def makeFig():                  # Create a function that makes our desired plot
    plt.ylim(0, 20)             # Set y-axis limit from 0 to 20
    plt.title('Live Graph')     # Give a title to the graph
    plt.ylabel('Values from SampleFile')
    plt.xlabel('Time')                             
    plt.plot(liveData, 'bo-', label='Label for Data')  # b=blue,o=dot,-=line
    plt.legend(loc='upper right')                    # location of the label
    plt.show()


while True:
    graph_data = open('sampleFile2.txt', 'r').read()
    # Take the data of one row in 'lines'
    lines = graph_data.split('\n')       # split this by new line
    
    lastLine = len(lines)             # Get the number of elements or length
    if lines[lastLine-1] > 0:         # To check last element is present or not
        liveData.append(lines[lastLine-1])
                
    drawnow(makeFig, show_once=True)    # call drawnow to update our live graph
    plt.pause(.000001)                  # wait for a short time

    cnt = cnt + 1             # Increment the count for each append
    if cnt > 5:               # To get last five data readings only
        liveData.pop(0)       # Clear the last data by popping it out
