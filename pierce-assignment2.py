##Harrison Pierce
##This program calculates the factorial of a user defined number

##Set factorial variable to 1
factorial = 1

k = int(input('Enter a postitive integer: '))
##Ask user for an integer and set equal to the variable k


for k in range(1,k + 1):
##start for loop for k. while between 1 and the number entered continue to stay in loop
	factorial = factorial * k
##multiply the number entered by k and each time add 1 to k
##until the numbner entered by the user is reached.
print("The factorial of the number entered is ", factorial)
##Print the product of the factorial.
##------------------------------------------------------------------------------
##Question 2
##Create variable i and set equal to user input for number of rows desired
i = int(input('Enter the number of rows: '))
##create for loop that stays in loop until i is reached
for row in range(i):
##print a pound sign for the column on the left 
	print('#', end='', sep='')
##this loop prints the appropriate number of spaces for the current iteration in the
##outter for loop. 
	for spacenum in range(row):
##print a space
		print(' ', end='', sep="")
##print the pound sign after reaching the appropriate number of spaces for the row
	print('#', sep='')
