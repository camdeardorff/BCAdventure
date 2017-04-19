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
			if not dilemma.hasActions():
				print("Malformed dilemma, contains no actions. Dilemma: ", dilemma)
			else:
				# provided dilemma has an action, show it and get a choice from the user
				self.__showDilemma(dilemma)
				userChoice = self.__getBinaryInputFromMessage("")
				# act on the user's choice
				if self.debug and userChoice == -1:
					# debug mode, -1 meand to go up the tree
					chosenAction = dilemma.getParent().getParent().getParent()
				else:
					chosenAction = dilemma.getActions()[userChoice]
					# determine what to do with the action selected
					if chosenAction.hasDilemma():
						# recurssive move down to the dilemma of the chosen action
						chosenDilemma = chosenAction.getDilemma()

						# check if this dilemma references another one
						# normally this is not the case
						if not chosenDilemma.hasReference():
							# the dilemma does not reference another dilemma, this is normal case
							self.__nextStep(chosenDilemma)

						else:
							# the dilemma points to another one by id reference
							# get the dilemma that was referenced
							referencedDilemma = self.adventure.findDilemmaWithID(chosenDilemma.getReference())
							# check whether or not the referenced dilemma is a good one
							if referencedDilemma == None:
								print("Failed to get dilemma referenced with an ID of ", chosenDilemma.getReference())
							else:
								self.__nextStep(referencedDilemma)

					# this action does not have a dilemma, it has a resolution. End the game		
					elif chosenAction.hasResolution():
						self.__showResolution(chosenAction.getResolution())
					else:
						print("Malformed action, contains no dilemma, or resolution. Action: ", chosenAction)
			


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
		if self.debug != True:
			for character in message:
				sys.stdout.write( character )
				sys.stdout.flush()
				time.sleep(random.random() * 0.15)
		else:
			print(message)







			