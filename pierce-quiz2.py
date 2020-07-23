##Harrison Pierce
##This program calculates the estimated price of tuition
##each year in a 5 year period beginning with $8000
##and increasing 3% each year

##create variable for base tuition and set equal to 8000
tuition = 8000
##set year to 1 since we are starting on the first of 5 years
year = 1

for x in range(5):	##loop begins at 0, we set x and put 5 in range
	year = x + 1	##add 1 year each loop
	print('Tuition for year', year, 'is', format(tuition, '.2f'))
##above we print the tuition and year while formatting the price to 2 decimal places
	tuition = (tuition + (tuition * .03))	##arithmetic for calculating tuition each year
	year + 1	##add 1 to the year as the loop completes

##-----------------------------------------------------------------------

##Question 2

import turtle
length = 5	##Base length set to 5
angle = 90	##Andle of turn to 90 degrees

for x in range(42):
	turtle.forward(length+length)	##move forward the appropriate amount
	turtle.left(angle)				##turn left
	length = length + 5				##add 5 to the length of line and repeat loop again
