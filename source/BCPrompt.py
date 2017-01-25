

class BCPrompt:

	__type = "prompt"

	def __init__(self, messages, parent):
		self.messages = messages;
		self.parent = parent	

	# BCPrompt getters
	def getMessages(self):
		return self.messages

	def getParent(self):
		return self.parent

	def getType(self):
		return self.__type

	# BCPrompt getters
	def setParent(self, parent):
		self.parent = parent

	# BCPrompt property state convenience methods
	def hasMessages(self):
		return self.getMessages() != None and len(self.getMessages()) > 0

	def hasParent(self):
		return self.getParent() != None
		

	def printall(self):
		if self.hasMessages():
			for message in self.getMessages():
				print("message: ", message)