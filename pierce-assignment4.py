##Harrison Pierce
#Assignment 4

##I have tried for a while to get this program to work. I think it is likely a 
#syntax error even though the logic should hold up. 

##Determines if a user defined number is prime or is not prime using a list.


#Collect a number from the user 	
usernum = int (input('Enter a number greater than 1: '))


#create the list and make as many spaces as there are equal to the number entered by user
numlist = [0] * usernum

#create the index variable to be used in determining where in the list the loop is
##create count variable for the while loop, starting at 2
index = 0
count = 2

#main function begin
def main():
#while loop to increase starting at 2, until the usernum is reached
	while count < usernum:

#for each iteration of the loop, set the item in the list at the index point
#equal to the count value for that iteration in the loop
		numlist[index] = count
#add 1 to count and 1 to index number until count is = to usernum
		count + 1
		index + 1
#restart/exit loop

##print(numlist)
##optionally, print list to see if its working, my program always gets stuck here
# and I cannot figure out why!

##define prime function and pass numlist from main
def prime(numlist):
#k variable is used as the index in the list 'numlist'
	k = 0
##create for loop that counts from every number from 2 to the number entered by the user.
	for x in range(2, usernum):
#here we determine if the number in the list is divisible by any one of the postitive
#lower than itself
		div = (numlist[k] % x)
#if statement that is enterd when the k item in numlist is determined to be divisible
#by x without a remainder and is thus not prime, x is set equal to usernum and 
#loop is exited
		if div == 0:
			print(usernum, 'is not prime')
			x = usernum
##if x is equal to the usernum the count has been through all numbers less than usernum
#print to tell user that the number is prime and has no factors less than itself
		elif x == usernum:
			print(usernum, 'is prime')
#add 1 to k so that the next item in numlist is tested for divisibility
		k + 1

main()
prime(numlist)