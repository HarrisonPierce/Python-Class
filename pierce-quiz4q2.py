##Harrison Pierce
##Quiz 4
 ##This program calculates the number of vowels and consonants 
 #in a string entered by the user.


##Define function to count vowels, pass userstring
def vowelcalc(string):
    
    vowel = 'aeiou'	#Define vowels
    vowelcount = 0
    
    
    for char in string:	#enter for loop for each character in the string
        if char.lower() in vowel:	#if character is in the string 'vowel',
        							#add 1 to the vowelcount
    
        	vowelcount += 1
    
    return vowelcount #return number of vowels
 
# calc_num_consonants accepts a string and returns the number of consonants.
# Note that this function does considers 'y' to be a consonant.
   
    #Define the function for calculating number of consonants in the user input
def consonantcalc(string):
    
    consonant = 'bcdfghjklmnpqrstvwxyz'	#define all the consonants
    consonantcount = 0					#define counter for consonants

    #enter the loop for the string and go through all characters
    for char in string:
    	#if a char is in the string 'consonant', add 1 to the counter
        if char.lower() in consonant:

            consonantcount += 1
    #return num of consonants
    return consonantcount
 
#Get user to enter a string to be used in counting vowels and consonants
userstring = input('Enter a string: ')
#Call each function to count the consonants and vowels
vowels = vowelcalc(userstring)
consonants = consonantcalc(userstring)
#print the number of each 
print('Vowels:', vowels, 'Consonants:', consonants)