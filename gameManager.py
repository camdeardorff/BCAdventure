from pathlib import Path
import xml.etree.ElementTree as etree  
import os

class GameManager:

	def __getGamesList(self):
		return os.listdir("games")

	# returns a list of game titles
	def getList(self):
		games = []
		gameFiles = self.__getGamesList()
		for gameFile in gameFiles:
			root = etree.parse("games/" + gameFile).getroot()
			name = root.get("title")
			games.append(name)
		return games


	def getPathOfGame(self, index):
		gameFiles = self.__getGamesList()
		if (-1 < index and index < len(gameFiles)):
			return "games/" + self.__getGamesList()[index]
		else:
			return None

	# when given an index of a game, returns the root node of the game
	def select(self, index):
		gameFiles = self.__getGamesList()
		if (-1 < index and index < len(gameFiles)):
			path = "games/" + gameFiles[index]
			return etree.parse(path).getroot()
		else:
			raise NameError("No such game, selection out of bounds")
			return None