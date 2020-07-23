##Harrison Pierce
##Assignment 5

##This program reads file named textfile and lists each word in the file
##in alphabetical order and counts the number of times they appear in the 
##file. 

#open the text file
file = open("textfile.txt","r")

#create dictionary for wordindex
wordindex={}
linenum = 0


#this for loop reads the contents of the file we opened
for line in file:	##line for the line number inside the file
	linenum = linenum + 1	#add 1 to the line number each time loop is started
	words=line.split()		#make the string into a list

	for index in range(0,len(words)):
		##continue in this loop for the entirety of the index for the words in the file
		##based on the line the text is on, add the linenum the index
		if words[index] in wordindex:
			if linenum not in wordindex[words[index]]:
				wordindex[words[index]].append(linenum)	
		else:
			wordindex[words[index]]=[linenum]
file.close()##close the text file



##output_file creates an object for the new file we create called "index" and opens in write mode

output_file=open('index.txt','w+')

#for loop writes the dictionary data from our text file to the new index file
for key in sorted(wordindex.keys()):	#key is used for the individual words logged
	output_file.write("%s:"%(key))
	for value in wordindex[key]:		##value is what the line numbers are saved in for the specific key
		output_file.write(' %d' %(value))
	output_file.write('\n')

output_file.close
##close the new file and save