#Harrison Pierce
#final question 2


#This program uses recursion to print asterisks for the number of 
#lines entered by the user, increasing in length by 1 for each line.

def main():

#Get input from user for desired number of lines to show
	lines = int(input("Enter the number of lines to display: "))
	printpattern(lines)
##call printpattern function and pass lines variable 

def printpattern(line):
	#if the user enters a number less than 1, the function ends 
	if (1 > line):	
		return

	#print the number of asterisks for a line 
	for i in range(0,line+1):
	#'i' indicates the line number, and the number of asterisks to be printed

		print('*'*i) #multiply 'i' by the asterisk to reach the correct number of *'s
		print(end='') #next line

#call main function

main()