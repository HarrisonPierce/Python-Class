#Harrison Pierce
#Final question 3
#couldnt get this program to run

class ship():

	def __init__(self, name, year):

		self.__name = name 
		self.__year = year

	def getName(self):	

		return self.__name
	

	def getYear(self):

		return self.__year

	def __str__(self):

		return print("ship name: " + self.__name + "year ship was built: " + self.__year)



class CruiseShip(ship):

	def __init__(self,name,year,num):

		super().__init__(name,year)
		self.__num = num


	def __str__(self):

		return print("Ship name: " + self.getName() + "Year ship was built: " + self.getYear()+"Max passengers: "+ self.__num)


class CargoShip(ship):

	def __init__(self,name,year,cap):

		super().__init__(name,year)
		self.__cap = cap

	def __str__(self):

		return print(super().__str__()+"Cargo capacity: "+self.cap)


def testfunction( ):

	s1 = ship("RMS Lusitania", 1902)

	s2 = CruiseShip("RMS Titanic", 1903, 1100)

	s3 = CargoShip("RMS Olympic", 1900, 1000)

	s1.__str__();

	s2.__str__();

	s3.__str__();