##Harrison Pierce
##Create quantity variable and set equal to user input for packages purchased
quantity = int(input("How many packages are being purchased? "))

##Below is a series of if elif statements which start by determining if the 
##quantity entered is within the requirements of the if statement. If it is,
##the 'if' statement is entered and the total price is calculated by multiplying
##the package price by the appropriate discount for that number of packages being sold
##Once the arithmetic is completed, the total price is displayed to the hundredths place
##and the percentage discount is shown to the customer 
if quantity <= 9:
	quantity = (quantity * 99)
	print('Your total is $', format(quantity, '.2f')) ##.2f makes sure only printed to the hundreds place
	print('The discount is 0%') ##print discount amount
elif 10 <= quantity <= 19:
	quantity = quantity * (99 * .80)
	print('Your total is $', format(quantity, '.2f'))
	print('The discount is 20%')	
elif 20 <= quantity <= 49:
	quantity = quantity * (99 * .70)
	print('Your total is $', format(quantity, '.2f'))
	print('The discount is 30%')	
elif 50 <= quantity <= 99:
	quantity = quantity * (99 * .60)
	print('Your total is $', format(quantity, '.2f'))
	print('The discount is 40%')	
elif quantity >= 100:
	quantity = quantity * (99 * .50)
	print('Your total is $', format(quantity, '.2f'))
	print('The discount is 50%')