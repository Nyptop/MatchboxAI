import random
class Matchboxes():

	def __init__(self):
		#allGames = self.createAllGames()
		self.allGames = {}
		self.createAllGames()
		self.gameStates = [] # list of strings which are the keys for every
		#game state in the game. Use these to go back and adjust bead counts 
		#depending on loss or victory
		self.movesMade = [] #list of integers for every move made in the game

	def createAllGames(self):
		dictio = {}
		beads = ''
		for a in range(0,10):
			beads = beads + '0'
		for b in range(0,10):
			beads = beads + '1'
		for c in range(0,10):
			beads = beads + '2'
		for d in range(0,10):
			beads = beads + '3'
		for e in range(0,10):
			beads = beads + '4'
		for f in range(0,10):
			beads = beads + '5'
		for g in range(0,10):
			beads = beads + '6'
		for h in range(0,10):
			beads = beads + '7'
		for i in range(0,10):
			beads = beads + '8'		
		chars = ['X',' ','O']
		#key to be a string of the game, which can be converted into a list 
		#create all possible strings of length 2 using the 3 characters above
		newKey = ''
		for i in range(0,3):
			for j in range(0,3):
				for k in range(0,3):
					for l in range(0,3):
						for m in range(0,3):
							for n in range(0,3):
								for o in range(0,3):
									for p in range(0,3):
										for q in range(0,3):
											newKey = newKey + chars[i] +chars[j] +chars[k]+chars[l]+chars[m]+chars[n]+chars[o]+chars[p]+chars[q]
											if len(newKey)==9:
												dictio[newKey]=beads
												newKey = ''
		self.allGames = dictio

	def returnMove(self, gameState):
		gameStateAsStr = ''
		for val in gameState:
			gameStateAsStr = gameStateAsStr + val
		self.gameStates.append(gameStateAsStr)
		#return a list of the new game state once the Matchbox
		#AI's move has been made
		beads = self.getBeadsFromMatchbox(gameStateAsStr) #find Matchbox (dict) corresponding to game state
		bead = self.selectBead(beads)
		whileCount = 0 
		while not self.isEmpty(bead, gameStateAsStr):
			#print("PlaceTaken")
			bead = self.selectBead(beads)
			if whileCount > 20:
				bead = self.selectRandomBead(beads)
			whileCount+=1
			#print(whileCount)
			if whileCount>200:
				break
			#newBoard = self.placeBead(bead, gameStateAsStr)
		#print("choosing " +str(bead))
		self.movesMade.append(bead)
		return bead #this new board goes to game.py as the chosen move

	def getBeadsFromMatchbox(self, gameStateStr):
		#goes into big dictionary and finds beads for the gameState
		beads = self.allGames[gameStateStr]
		return beads

	def selectBead(self, beads):
		#chooses a bead from a list of beads
		#print(len(beads))
		#if len(beads)<2:
		#	print("Running low on beads")
		#if len(beads)>70 and len(beads)<80:
		#	print("Learning")
		if len(beads)>2:
			index = random.randint(0,len(beads)-1)
		#print("Selecting bead at... "+str(index))
			return beads[index]
		else:
			return beads[0]

	def selectRandomBead(self, beads):
		randomBead = random.randint(0,8)
		#print("Random: "+str(randomBead))
		return randomBead

	def isEmpty(self, bead, board):
		index = int(bead)
		if board[index] == ' ':
			return True
		else:
			return False


	def placeBead(self, bead, board):
		index = int(bead)
		newBoard = board[:index] + 'X' + board[index+1:]
		#s = s[:index] + newstring + s[index + 1:]
		return newBoard
		#returns a board with the bead on it

	###below will be the learning portion of the class###
	#if this program wins a game, it increases the count of each of the letters it played
	#by 3
	def win(self):
		iteration = 0
		for state in self.gameStates:
			#pull out the matchbox
			currentMatchbox = self.allGames[state]
			# select 2 beads
			newBeads = self.movesMade[iteration] * 4
			iteration += 1
			# add the beads
			newMatchbox = currentMatchbox + str(newBeads)
			# put matchbox away
			self.allGames[state] = newMatchbox
		self.reset()

	def lose(self):
		iteration = 0
		for state in self.gameStates:
			#pull out the matchbox
			currentMatchbox = self.allGames[state]
			# select bead
			beadToRemove = str(self.movesMade[iteration]) 
			iteration += 1
			# remove 2 beads (if there are 3 beads)
			if len(self.allGames[state])>2:
				if beadToRemove in currentMatchbox:
					newMatchbox = currentMatchbox.replace(beadToRemove,'',2)
					# put matchbox away
					self.allGames[state] = newMatchbox
		self.reset()

	def reset(self):
	#after each game, reset
		self.gameStates = []
		self.movesMade = []

#### functions for playing against the matchbox AI once fully trained

