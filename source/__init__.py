from BCParser import BCParser
from BCGame import BCGame
import sys

debugMode = "cam"

parser = BCParser('../xml/testGame.xml')
adventure = parser.getAdventure()

game = BCGame(adventure, debugMode in sys.argv)
game.start()