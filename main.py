from BCAdventure.BCTreeValidator import BCTreeValidator
from BCAdventure.BCParser import BCParser
from BCAdventure.BCGame import BCGame
import sys

from gameManager import GameManager

debugMode = "-debug"

def isDebug():
	debugMode in sys.argv

def showGameList(games):
	print("Available games: ")
	for index, game in enumerate(games):
		print("(", index, ") ", game)

def getSelection():
	print("Please enter the number associated with the game you would like to play")
	selection = None
	while(selection is None):
		try:
			selection = int(input())
		except ValueError:
			print("That input does not correspond to a playable game, try again.")
	# selection is not none
	return selection

def validateGame(path):
	validator = BCTreeValidator(path)
	return validator.validate()


def getGame(gameManager, selection):
	game = None
	while(game is None):
		try:
			game = gm.select(selection)
			print(game)
		except NameError as err:
			print(err)
			print("Please try again.")
	# game has been successfully retrieved
	return game



print("--- BCAdventure ---")


gm = GameManager()
# print(gm.getList())
gameList = gm.getList()
if (len(gameList) < 1):
	print("There are no playable games.")
else:

	newGame = True

	while (newGame):

		showGameList(gameList)
		userSelection = getSelection()
		path = gm.getPathOfGame(userSelection)

		if (path is not None and validateGame(path)):
			# get the game from game 
			game = gm.select(userSelection)
			# parse the game 
			parser = BCParser(game)
			# extract the adventure from the parser
			adventure = parser.getAdventure()
			# start the game session
			session = BCGame(adventure, isDebug())
			session.start()

			print("Would you like to play another game? (Yes, No)")
			newGame = (input() == "Yes")
		else:
			print("Game file is not valid, please select another game.")


	