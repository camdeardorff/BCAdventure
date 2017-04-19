
class BCAction:

	__type = "action"

	def __init__(self, message, dilemma, resolution, parent):
		self.message = message
		self.dilemma = dilemma
		self.resolution = resolution
		self.parent = parent

		if self.hasDilemma():
			self.dilemma.setParent(self)
		if self.hasResolution():
			self.resolution.setParent(self)

	# BCAction getters
	def getMessage(self): 
		return self.message

	def getDilemma(self):
		return self.dilemma

	def getResolution(self):
		return self.resolution

	def getParent(self):
		return self.parent

	def getType(self):
		return self.__type

	# BCAction setters
	def setDilemma(self, dilemma):
		self.dilemma = dilemma

	def setParent(self, parent):
		self.parent = parent

	# BCAction property state convenience methods
	def hasMessage(self):
		return self.getMessage() != None

	def hasDilemma(self):
		return self.getDilemma() != None

	def hasResolution(self):
		return self.getResolution() != None

	def hasParent(self):
		return self.getParent() != None


	def printall(self):
		if self.hasMessage():
			print("action: ", self.getMessage())
		if self.hasDilemma():
			print("- dilemma: ", self.getDilemma().printall())
		if self.hasResolution():
			print("- resolution: ", self.getResolution().printall())

