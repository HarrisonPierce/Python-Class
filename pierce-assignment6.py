##Harrison Pierce
##Assignment 6


#This program lets a user add, edit, delete and look up employees

class Employee:
	def __init__(self, name, idnum, department, jobtitle):

		self.name = name
		self.idnum = idnum
		self.department=department
		self.jobtitle = jobtitle
##set all objects

	def setname(self, placehold):
		self.name=placehold

	def setidnum(self, placehold):
		self.idnum=placehold

	def setdepartment(self, placehold):
		self.department=placehold

	def setjobtitle(self, placehold):
		self.jobtitle=placehold
## functions to set each variable when called


	userdata = dict()
## create dictionary
	def add():
# fuction to add employee
		name=input("Name: ")
		ID = input("ID num: ")
		dep = input("Department: ")
		job = input("job title: ")

#fuction to loop up employee
	def lookup():

		inp = input("Enter ID number to look up: ")
		if inp in userdata.keys():
		#get id num from user and search dictionary for input 
			print(userdata[inp])
		
		else:

			print("ID number not found in dictionary")
## display if ID isnt found
	def edit():
#fuction to edit employees
		inp = input("Enter ID number to update: ")

		if inp in userdata.keys():
#find inp from user in dictionary
			print("Enter updated data...")
			
			name = input("Name: ")
			userdata[inp].setname(name)

			department = input("Department: ")
			userdata[inp].setdepartment(dep)

			jobtitle = input("Job title: ")
			userdata[inp].setjobtitle(jobtitle)

		else:
			print("ID is not valid")

	def delete():
#delete function
		inp = input("Enter ID number to delete: ")
#get input from user
		if inp in userdata.keys():
			del userdata[inp]
#search for id num in dictionary and delete
	

#set x to be used in sentinal loop
	x = 1

	while x == 1:
#enter loop since x is 1
		print("Enter 'A' to add Employee")
		print("Enter 'L' to look up an employee")
		print("Enter 'E' to edit employee ")
		print("Enter 'D' to delete an employee")
		print("Enter 'Q' to quit")
#give user an options list
		choice = input()

		if choice == "A":
			add()
			print()

		if choice == "L":
			lookup()
			print()
		if choice == "E":
			edit()
			print()
		if choice == "D":
			delete()

		if choice == "Q":
			x = 0
			#exit loop by setting x to 0

##depending on the user input, enter the appropriate if statement