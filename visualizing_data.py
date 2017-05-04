import matplotlib.pyplot as plt 
from collections import Counter 

def make_chart_simple_line_chart(plt):

	#function to graph gdp in a line chart
	#this is the gdp data 

	years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
	gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 149583.3]

	plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

	plt.title("Nominal GDP")
	plt.ylabel("Billions of $")
	plt.show()


if __name__ == '__main__':
    make_chart_simple_line_chart(plt)
