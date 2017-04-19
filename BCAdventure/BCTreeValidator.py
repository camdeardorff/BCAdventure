import xml.etree.ElementTree as ET

class BCTreeValidator:

	def __init__(self, filename):
		self.finename = filename
		self.root = ET.parse(filename).getroot()
		self.validTags = ['resolution', 'prompt', 'message', 'action', 'adventure', 'dilemma', 'actions']

	def validate(self):
		tags = self.__getTagList()
		for tag in tags:
			if tag not in self.validTags:
				print("tag with name: ", tag, " is not valid")
				return False
		return self.__isValidateStructure(self.root)


	def __getTagList(self):
		import xml.etree.ElementTree as ET

		elemList = []

		for elem in self.root.iter():
		  	elemList.append(elem.tag)

		# remove duplicities - by convertion to set and back to list
		return list(set(elemList))


	def __isValidateStructure(self, item):
		'''
		recurssive tree search that returns a boolean
		'''

		if item == None:
			print(" item is none ")
		else:
			tag = item.tag

			if tag == "adventure":
				'''
				 	attr
				 		title
					children
						dilemma
				'''

				title = item.get("title")
				dilemma = item.find("dilemma")

				if title is None:
					print(tag, " has not attribute 'title'. ")
					return False
				elif dilemma is None:
					print(tag, " with title: ", title, ", does not have a dilemma")
					return False
				else:
					return self.__isValidateStructure(dilemma)
				

			elif tag == "dilemma":
				'''
				 	attr
				 		id (optional)
				 		ref (optional)
				 		# id/ref -> mutually exclusive
					children
						prompt
						actions
				'''

				identifier = item.get("id")
				reference = item.get("href")
				prompt = item.find("prompt")
				actions = item.find("actions")

				# mutex for identifier and reference
				if (identifier is None and reference is None or 
				identifier is not None and reference is not None):
					print(tag, " must have either an id or an href, not both and not neither")
					return False

				else:
					if (identifier is not None):
						# if identifier is not none then it should have a prompt and actions
						if prompt is None:
							print(tag, " with id: ", identifier, ", does not have a prompt")
							return False
						elif actions is None:
							print(tag, " with id: ", identifier, ", does not have a actions")
							return False
						else:
							return (self.__isValidateStructure(prompt) 
								and self.__isValidateStructure(actions))

					elif (reference is not None):
						# if this dilemma has a reference then it should not have a prompt or actions
						if prompt is not None:
							print(tag, " with href: ", reference, ", has a prompt")
							return False
						elif actions is not None:
							print(tag, " with href: ", reference, ", has an actions")
							return False
						else:
							return True


			elif tag == "prompt":
				'''
					children
						message(s) (list of messages)
				'''

				messages = item.findall("message")
				if (len(messages) < 1):
					print(tag, " must have at least one message")
					return False
				else:
					return True

			elif tag == "actions":
				'''
				 	children
				 		action(s) (list of actions)
				'''

				actions = item.findall("action")
				if (len(actions) is not 2):
					print(tag, " must have at two action")
					return False
				else:
					return (self.__isValidateStructure(actions[0]) 
						and self.__isValidateStructure(actions[1]))



			elif tag == "action":
				''' 
					children
						message
						dilemma (optional)
						resolution (optional)
						# dilemma/resolution -> mutually exclusion
				'''

				message = item.find("message")
				dilemma = item.find("dilemma")
				resolution = item.find("resolution")

				if (dilemma is None and resolution is None or 
				dilemma is not None and resolution is not None):
					print(tag, " must have either a dilemma or a resolution, not both and not neither")
					return False
				elif (message is None):
					print(tag, " must have a message")
					return False
				else:
					if (dilemma is not None):
						return self.__isValidateStructure(dilemma)
					elif (resolution is not None):
						return self.__isValidateStructure(resolution)

			elif tag == "resolution":

				return True

