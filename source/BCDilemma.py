

class BCDilemma:

	__rootID = 0
	__type = "dilemma"


	def __init__(self, reference, identity, prompt, actions, parent):
		self.identity = identity
		self.reference = reference
		self.prompt = prompt
		self.actions = actions
		self.parent = parent

		if self.hasPrompt():
			self.prompt.setParent(self)
		if self.hasActions():
			for action in self.getActions():
				action.setParent(self)

	# BCDilemma property getters
	def getID(self):
		return self.identity

	def getReference(self):
		return self.reference

	def getPrompt(self):
		return self.prompt

	def getActions(self):
		return self.actions

	def getParent(self):
		return self.parent

	def getType(self):
		return self.__type

	# BCDilemma property getters
	def setParent(self, parent):
		self.parent = parent

	# BCDilemma property state convenience methods
	def hasID(self):
		return self.getID() != None

	def hasReference(self):
		return self.getReference() != None

	def hasPrompt(self):
		return self.getPrompt() != None

	def hasActions(self):
		return self.getActions() != None and len(self.getActions()) > 0

	def hasParent(self):
		return self.getParent() != None

	def isRoot(self):
		return self.getID() == __rootID

	def tostring(self):
		return "id: ", self.getID(), ", referenece: ", self.getReference(), ", has prompt: ", self.hasPrompt(), ", has actions: ", self.hasActions()

	def printall(self):
		if self.hasID():
			print("dilemma id: ", self.getID())

		if self.hasReference():
			print("- Reference: ", self.getReference())

		if self.hasPrompt():
			print("- prompt: ", self.getPrompt().printall())

		if self.hasActions():
			for action in self.getActions():
				print("- action: ", action.printall())