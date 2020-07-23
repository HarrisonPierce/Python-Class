#Harrison Pierce
#Quiz 5
##This program generates random numbers in the range 0-100 and 
#verifies if there are any duplicates

import random
#random used to generate numbers
dic = []
#create dictionary


##for loops 10 times, one for each number
for x in range(10):
    #generate the random int in range 1-99
    i = random.randint(1,99)
    #add random num, i, to the dictionary
    dic.append(i)

#print dictionary values
print('The dictionary values are:')
print(dic)


##Check for duplicates
duplicate = False


for x in range(10):
    for y in range(x+1,10):

        #compare values of dictionary index x and x+1, or 1 greater than x, 
        #for equity
        if dic[x] == dic[y]:
            duplicate = True
##If duplucate is found, print appropriate message

if duplicate == False:
    print("There are no duplicate values in the dictionary")
else:
    print('There are duplicate values in the dictionary')

#------------------------------------------------------------------------------
#Q2 
# I do not have enough keyboard symbols to match with all alphabet leters, capital and noncap
# I searched online and found a pre-made dictionary set with enough symbols to match letters
# No plagiarism intended here!! The rest is my work

codes = {

    'A' : '%',

    'a' : '9',

    'B' : '@',

    'b' : '#',

    'C' : '!',

    'c' : '1',

    'D' : '$',

    'd' : '7',

    'E' : '`',

    'e' : '5',

    'F' : '&',

    'f' : '3',

    'G' : "'",

    'g' : '6',

    'H' : '(',

    'h' : '2',

    'I' : ')',

    'i' : '8',

    'J' : '*',

    'j' : '4',

    'K' : '+',

    'k' : '¡',

    'L' : ',',

    'l' : '¢',

    'M' : '-',

    'm' : '£',

    'N' : '.',

    'n' : '¥',

    'O' : '/',

    'o' : '¦',

    'P' : ':',

    'p' : '§',

    'Q' : ';',

    'q' : '©',

    'R' : '<',

    'r' : '«',

    'S' : '=',

    's' : '¬',

    'T' : '>',

    't' : '®',

    'U' : '?',

    'u' : '±',

    'V' : '[',

    'v' : 'µ',

    'W' : '\\',

    'w' : '¶',

    'X' : ']',

    'x' : '¿',

    'Y' : '^',

    'y' : 'Æ',

    'Z' : '_',

    'z' : '»',

    '%' : 'A',

    '9' : 'a',

    '@' : 'B',

    '#' : 'b',

    '!' : 'C',

    '1' : 'c',

    '$' : 'D',

    '7' : 'd',

    '`' : 'E',

    '5' : 'e',

    '&' : 'F',

    '3' : 'f',

    "'" : 'G',

    '6' : 'g',

    '(' : 'H',

    '2' : 'h',

    ')' : 'I',

    '8' : 'i',

    '*' : 'J',

    '4' : 'j',

    '+' : 'K',

    '¡' : 'k',

    ',' : 'L',

    '¢' : 'l',

    '-' : 'M',

    '£' : 'm',

    '.' : 'N',

    '¥' : 'n',

    '/' : 'O',

    '¦' : 'o',

    ':' : 'P',

    '§' : 'p',

    ';' : 'Q',

    '©' : 'q',

    '<' : 'R',

    '«' : 'r',

    '=' : 'S',

    '¬' : 's',

    '>' : 'T',

    '®' : 't',

    '?' : 'U',

    '±' : 'u',

    '[' : 'V',

    'µ' : 'v',

    '\\': 'W',

    '¶' : 'w',

    ']' : 'X',

    '¿' : 'x',

    '^' : 'Y',

    'Æ' : 'y',

    '_' : 'Z',

    '»' : 'z'}


#set textfile to open the unencrypted text file in read only
textfile = open("unencryptedtext.txt","r")

#read unencryptedtext.txt, point to text
text = textfile.read()

#open and create the encryptedtext.txt file in write only, and point to k
k = open("encryptedtext.txt","w")

#read from the input file for the entire length of the text.
for i in range(len(text)):

    #write to encryption if the value is found in the key
    if text[i] in codes:
        k.write(codes[text[i]])
        ##write the code coresponding to the character found in text[i] 


textfile.close()
k.close()
#close the opened files

