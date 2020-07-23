##QUESTION 2

##get user input for variables

height = int(input('please enter height in inches: '))
weight = int(input('please enter weight in pounds: '))

BMI = weight * 703 // (height * height)
##Arithmetic for BMI Calculation
##Also sets BMI variable up for if statements

if 18.5 < BMI < 25:
	print('Your weight is optimal')
elif BMI <= 18.5:
	print('You are underwight')
elif BMI >= 25:
	print('You are overweight')

##decides if BMI is optimal, under, or overweight.