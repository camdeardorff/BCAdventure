import xml.etree.ElementTree as ET
from BCAdventure import BCAdventure
from BCDilemma import BCDilemma
from BCPrompt import BCPrompt
from BCAction import BCAction
from BCResolution import BCResolution
import copy


class BCParser:

	def __init__(self, filename):
		self.filename = filename;
		self.root = ET.parse(filename).getroot()

	def __recursiveConstruction(self, parent, item):
		if item == None:
			return None
		else:

			tag = item.tag

			if tag == "adventure":
				dilemma = self.__recursiveConstruction(item, item.find("dilemma"))
				title = item.get("title")
				return BCAdventure(title, dilemma)

			elif tag == "dilemma":
				identity = item.get("id")
				reference = item.get("href")
				prompt = self.__recursiveConstruction(item, item.find("prompt"))
				actions = self.__recursiveConstruction(item, item.find("actions"))
				return BCDilemma(reference, identity, prompt, actions, parent)

			elif tag == "prompt":
				messages = []
				for message in item.findall("message"):
					messages.append(message.text)
				return BCPrompt(messages, parent)

			elif tag == "actions":
				actions = []
				for action in item.findall("action"):
					actions.append(self.__recursiveConstruction(item, action))
				return actions

			elif tag == "action":
				message = item.find("message").text
				resolution = self.__recursiveConstruction(item, item.find("resolution"))
				dilemma = self.__recursiveConstruction(item, item.find("dilemma"))
				return BCAction(message, dilemma, resolution, parent)

			elif tag == "resolution":
				message = item.text
				return BCResolution(message, parent)

			else:
				return


	def getAdventure(self):
		adventure = self.__recursiveConstruction(None, self.root)
		return adventure


