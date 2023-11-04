import random

easy = {'board0': [[4,2,7,0,0,5,6,0,3],[1,0,0,0,0,6,0,0,0],[0,6,8,3,0,0,1,0,0],[2,0,0,3,4,0,8,0,1],[0,1,0,0,6,7,0,5,0],[4,0,0,0,5,1,0,2,0],[0,9,0,7,0,4,0,3,2],[0,0,0,3,0,0,0,9,4],[7,3,0,2,0,9,6,0,0]],
'board1': [[5,0,0,0,4,0,8,0,0],[6,7,0,8,0,0,5,0,0],[9,0,0,0,0,0,6,1,3],[0,6,2,1,0,0,3,7,4],[4,0,0,0,0,3,9,0,8],[0,7,0,0,2,0,0,0,0],[0,9,6,2,1,8,0,5,0],[1,0,7,0,0,6,0,8,0],[8,0,2,0,4,5,0,9,0]],
'board2': [[0,0,0,6,8,0,0,1,9],[0,0,0,4,7,0,5,0,8],[0,8,0,0,2,0,6,4,7],[0,6,0,3,4,2,1,9,0],[9,0,0,6,8,0,0,5,0],[0,0,4,0,0,0,8,3,0],[0,0,0,0,0,6,0,0,3],[7,2,0,0,0,5,8,9,1],[4,0,3,0,1,0,5,0,0]]}

medium = {'board0':[[0,0,0,0,0,2,5,0,6],[4,0,0,0,0,0,9,0,0],[2,0,0,0,1,8,0,3,0],[0,6,9,0,5,0,8,0,0],[0,0,0,0,0,0,1,5,7],[3,0,0,0,2,1,6,0,9],[0,0,0,9,0,0,0,0,0],[0,3,0,6,0,2,0,0,0],[9,6,0,0,5,0,7,0,2]],
'board1': [[2,5,0,3,0,9,0,0,1],[0,0,3,0,0,0,0,0,6],[0,9,1,7,2,0,3,0,0],[0,0,0,0,1,0,6,0,3],[0,6,8,0,4,0,0,0,0],[0,0,3,0,0,0,0,5,0],[1,3,2,0,0,0,7,6,4],[0,0,0,0,0,4,0,1,0],[0,7,0,0,6,0,0,0,0]]}

hard = {'board0':[[9,0,0,0,0,0,0,7,0],[0,1,0,0,6,0,9,0,8],[0,7,0,0,2,4,0,0,0],[0,0,6,2,1,8,0,5,3],[0,0,0,0,0,0,2,0,4],[0,0,0,0,0,0,6,0,0],[0,0,0,0,0,0,5,0,0],[5,4,9,0,0,0,0,0,0],[0,0,0,7,0,2,0,8,0]],
'board1': [[0,0,0,8,0,1,6,0,0],[6,0,0,0,0,7,0,0,4],[0,2,0,9,0,0,1,0,0],[0,0,5,0,2,8,0,0,0],[0,0,8,5,6,0,0,0,0],[0,0,0,4,0,3,0,8,0],[0,0,0,0,0,0,1,5,0],[0,9,0,7,0,0,0,0,0],[0,0,7,0,1,0,0,0,4]]}

expert = {'board0':[[7,6,0,5,0,0,0,3,0],[1,0,0,0,7,4,0,0,0],[5,0,8,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,3],[6,5,8,0,0,0,0,0,0],[0,0,0,0,0,0,2,0,4],[0,7,0,0,0,0,0,0,0],[2,0,0,5,0,0,0,0,3],[0,0,0,0,0,6,0,9,1]],
'board1': [[0,0,0,0,0,4,0,0,7],[0,0,4,0,3,0,0,0,0],[0,6,0,1,0,0,0,0,2],[0,0,5,0,0,0,0,8,0],[7,0,0,0,0,0,0,6,0],[9,2,0,0,0,0,0,0,0],[7,0,0,6,0,0,0,0,0],[0,0,0,9,0,5,0,4,0],[0,8,0,0,3,0,2,1,0]]}

def get_board(level):
	try:
		if(level.upper()=='EASY'):
			return(easy[str("board"+str(random.randint(0, (len(easy)-1))))]) 
		if(level.upper()=='MEDIUM'):
			return(medium[str("board"+str(random.randint(0, (len(medium)-1))))]) 
		if(level.upper()=='HARD'):
			return(hard[str("board"+str(random.randint(0, (len(hard)-1))))])
		if(level.upper()=='EXPERT'):
			return(expert[str("board"+str(random.randint(0, (len(expert)-1))))])
		else:
			raise NameError('Unknown Level: '+level.upper())
	except NameError:
		print("No board found")
		raise
	return('')