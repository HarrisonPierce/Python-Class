##Harrison Pierce
##Quiz 4
##This program asks for a user input of a string without spaces
#Every time a letter is capitalized in the string, a space is inserted.


#Accept user input of a string without spaces
string = input("Enter a string: ")


x = 0 #Create x variable to be used for counting the character in the string
result = ""


for char in string: ##Enter for loop and use 'char' for each character

    #If statement to add a space when there is an uppercase letter unless
    #its the first character
    if char.isupper() & x > 0:
        result += " "
        
        result += char.lower()
    ##next char in string
    else:
        result += char
    ##Add 1 to character count in string
    x += 1
##print final sentence with spaces
print (result)