
import time
import sys
import random


class BCGame:

	def __init__(self, adventure, debug):
		self.adventure = adventure
		self.debug = debug


	def start(self):
		print("starting game, in debug: ", self.debug)

		if self.adventure == None:
			return
		else:
			# ask if they would like to play
			message = "Would you like to play '" + self.adventure.getName() + "' ?\n[0] No\n[1] Yes"
			response = self.__getBinaryInputFromMessage(message)

			if not response:
				print("Goodbye")
				return
			else:
				self.__creepyPrint("Let's play! Starting now!\n\nYou go home...")
				if self.adventure.hasDilemma():
					self.__nextStep(self.adventure.getDilemma())


	def __getBinaryInputFromMessage(self, message):

			choice = None
			while choice == None:
				print(message)
				response = input()

				if response == "1":
					choice = 1
				elif response == "0":
					choice = 0
				elif self.debug and response == "up":
						choice = -1
				else:
					print("That doesn't appear to be an option, try again.")
			return choice



	def __nextStep(self, dilemma):
		if dilemma == None:
			return
		else:
			if dilemma.hasActions():
				self.__showDilemma(dilemma)
				choice = self.__getBinaryInputFromMessage("")
				if choice == -1 and self.debug:
					chosenAction = dilemma.getParent().getParent().getParent()
				else:
					chosenAction = dilemma.getActions()[choice]


				if chosenAction.hasDilemma():
					self.__nextStep(chosenAction.getDilemma())
				elif chosenAction.hasResolution():
					self.__showResolution(chosenAction.getResolution())
				else:
					print("there is something wrong with action: ", chosenAction)
			else:
				print("there is something wrong with dilemma: ", dilemma)



	def __showDilemma(self, dilemma):
		if dilemma != None:
			if dilemma.hasPrompt():
				prompt = dilemma.getPrompt()
				if prompt != None:
					self.__showPrompt(prompt)
			if dilemma.hasActions():
				self.__creepyPrint(self.__actionsToChoiceStrings(dilemma.getActions()))


	def __showPrompt(self, prompt):
		if prompt != None:
			if prompt.hasMessages():
				for message in prompt.getMessages():
					self.__creepyPrint("\n" + message)




	def __actionsToChoiceStrings(self, actions):
		if actions != None and len(actions) > 0:
			choiceString = ""
			for index, action in enumerate(actions):
				if action.hasMessage():
					# if index != 0:
					choiceString += "\n"
					choiceString += "[" + str(index) + "] " + action.getMessage()
			return choiceString



	def __showResolution(self, resolution):
		if resolution == None:
			print("there is something wrong with resolution: ", resolution)
		else:
			if resolution.hasMessage():
				self.__creepyPrint(resolution.getMessage())
				print("\nGame Over")



	def __creepyPrint(self, message):
		for character in message:
			sys.stdout.write( character )
			sys.stdout.flush()
			time.sleep(random.random() * 0.15)


























