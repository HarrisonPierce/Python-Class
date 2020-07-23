##Harrison Pierce
##Harrison Pierce
#This program 

import pickle


def main():

	endfile = False


	input_file = open('numbers.txt', 'rb')


	while not endfile:
		try:
			num = pickle.load(input_file)

			display_data(num)
		except (ValueError, EOFError):

			endfile = True

	input_file.close()


def display_data(num):
	print(num)

#------------------------------------------------------- 


num1 = int (input('Enter a number: '))

try:

	perfect(num1)

except NameError:


##for loop from 1 to number entered. Each time, 1 is added, divide num1 and 
##if mod == 0 then enter number into array. once complete, add numbers together
##If total == num1, num1 is a perfect number

	def perfect(num1):

		x = 1
		print(x)

		for count in range(1, num1):

			factordecide = ((num1/2))

			print(factordecide)