from __future__ import print_function

import sys
if sys.version_info[:2] <= (2, 7):
	get_input = raw_input
else:
	get_input = input

import time
import sdkdict as ds
import sdksolver as ss

print("\n")
print("WELCOME TO SUDOKU SOLVER!")
print("PLEASE, ENTER THE DESIRED OPTION: EASY, MEDIUM, HARD OR EXPERT => ",end="")

level = get_input()

while(not(level.upper()=="EASY" or level.upper()=="MEDIUM" or level.upper()=="HARD" or level.upper()=="EXPERT")):
	print("Invalid option, try again => ",end="")
	level = get_input()
print("\n\n")

board = ds.get_board(level)

if len(board) > 0:
	print("INPUT BOARD: ")
	ss.print_board(board)
	print("\n")
	print("GET SOLUTION? (Y)/N => ",end="")
	
	solve = get_input()
	
	while(solve.upper()=="N"):
		print("WAITING.... (Y)/N => ",end="")
		solve = get_input()
	print("")
	print("PRINT ITERATIONS? Y/(N) => ",end="")
	it = get_input()
	if it.upper()=="Y":
		it = True
	elif it.upper() == "N":
		it = False
	else:	
		solve = False	
	print("")
	
	start = time.time()
	result,nb_it = ss.solve_sudoku(board,it)
	end = time.time()
	print("OUTPUT BOARD: ")
	ss.print_board(result)
	print("\n")
	print("Elapsed time: "+str(end-start)+"s")
	print("Number of iterations: "+str(nb_it))
	print("\n")