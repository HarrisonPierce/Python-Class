
##Change count game!

##define value for each coin
penny = 1
nickle = 5
dime = 10
quarter = 25
loop = 'y'


##start loop
while loop == 'y':

##Collect the number of each coin from user
	nump = int(input('enter number of pennies: '))
	numn = int(input('enter number of nickles: '))
	numd = int(input('enter number of dimes: '))
	numq = int(input('enter number of quarters: '))

##arithmatic for total coin value
	total = nump + (numn * nickle) + (numd * dime) + (numq * quarter)

##if statements which look at the total value and print message appropriately
	if total > 100:
		print("Thats more than one dollar, try again!")
	elif total == 100:
		print('Thats exacctly one dollar, you win!')
	elif total <= 100:
		print('Thats less than one dollar, try again!')

	loop = input("Play again? y or n: ")

