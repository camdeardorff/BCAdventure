
class BCResolution:

	__type = "resolution"


	def __init__(self, message, parent):
		self.message = message
		self.parent = parent

	# BCResolution getters
	def getMessage(self):
		return self.message

	def getParent(self):
		return self.parent

	def getType(self):
		return self.__type

	# BCResolution setters
	def setParent(self, parent):
		self.parent = parent

	# BCResolution property state convenience methods
	def hasMessage(self):
		return self.getMessage() != None

	def hasParent(self):
		return self.getParent() != None
		

	def printall(self):
		if self.hasMessage():
			print("- resolution: ", self.getMessage())