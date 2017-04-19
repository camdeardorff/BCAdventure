
class BCAdventure:

	__type = "adventure"

	def __init__(self, name, dilemma):
		self.name = name
		self.dilemma = dilemma

		if self.hasDilemma():
			self.dilemma.setParent(self)

	# BCAdventure getters
	def getName(self):
		return self.name

	def getDilemma(self):
		return self.dilemma

	def getType(self):
		return self.__type

	# BCAdventure setters
	def setDilemma(self, dilemma):
		self.dilemma = dilemma

	# BCAdventure property state convenience methods
	def hasName(self):
		return self.getName() != None

	def hasDilemma(self):
		return self.getDilemma() != None

	# BCAdventure methods
	def findDilemmaWithID(self, id):
		return self.__recursiveFindSubDilemmaWithID(self.getDilemma(), id)

	def __recursiveFindSubDilemmaWithID(self, item, id):
		# print("testing dilemma for id")
		if item != None:
			# print("-- id: ", item.getID())
			if item.getID() == id:
				# print("adventure: found dilemma with id: ", id)
				return item
			else:
				if item.hasActions():
					foundDilemma = None
					for action in item.getActions():
						# print("-- action!")
						if action.hasDilemma():
							possibleDilemma = self.__recursiveFindSubDilemmaWithID(action.getDilemma(), id)
							if possibleDilemma != None:
								foundDilemma = possibleDilemma
					return foundDilemma

		

	def printall(self):
		if self.hasName():
			print("Adventure name: ", self.getName())
		if self.hasDilemma():
			print("- dilemma: ", self.getDilemma().printall())