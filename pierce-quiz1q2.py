##Harrison Pierce
##This program determines the year and then determins if the month of 
##feburary has 28 or 29 days based on whether or not it is a leap year

year = int(input('Enter the year: '))
##using the modular %, determine if the year is divisible by 100
if (year % 100) == 0:
	if (year % 400) == 0: ##determine if the year is also divisible by 400. If so, print the numbenr of days in feburary
		print('It is a leap year and there are 29 days in Feburary')
elif (year % 4) == 0: ##if year is not divisible by 400 but is divisible by 4 and 100, print the number of days in feburary.
	print('It is a leap year and there are 29 days in Feburary')	
