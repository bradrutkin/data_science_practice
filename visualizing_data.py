import matplotlib.pyplot as plt 
from collections import Counter 

def make_chart_simple_line_chart(plt):

	# function to graph gdp in a line chart
	# this is the gdp data 

	years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
	gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 149583.3]

        # this is the 'style guide' for the chart
	# the line is green, the markers are circles and the line is solid
	# the matplotlib documentation can be used so the settings are tinkered
	# with, for example you can set marker = 's' for square 
	plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

        # these lines set the title as well as the label on the xaxis
	plt.title("Nominal GDP")
	plt.ylabel("Billions of $")

	# shows the plot if the rest of the code is good 
	plt.show()

# this at the bottom sets it so if the program is run the functions labeled
# bellow are run. You do not need to call them. 
if __name__ == '__main__':
    make_chart_simple_line_chart(plt)
