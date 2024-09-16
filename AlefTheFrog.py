import random

from typing import Tuple, List

SIZE = (5,8)

FROG = (1,0)
LAST_MOVE = (1,0)

WALLS = [(0,5),(1,3),(1,4),(2,2),(2,3),(2,7),(3,3),(4,3)]
PASSAGE = {"02":(4,0), "40":(0,2), "04":(2,4), "24":(0,4)}
MINES = [(3,2), (3,6), (3,7)]

EXIT = [(0,7), (4,7)]


STACK = []


class Solution:
	def __init__(self, x):
		self.path = x
		#self.position = x
		
	def func():
		pass


def next_move(x,y)->List[Tuple[int]]:
	def get_move(x, y)->List[Tuple[int]]:
		return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
		
	def is_valid(x, y)->bool:
		if not (0 <= x and x < SIZE[0]) or not (0 <= y and y < SIZE[1]):
			return False
		if (x,y) in WALLS:
			return False	
		if (x,y) in MINES:
			return False	
		return True
		

	def reverse_move(x,y)->bool:
		if (x,y) == LAST_MOVE:
			return True
		return False
	
	def tunnel(x,y)->Tuple[int]:
		if f"{x}{y}" in PASSAGE.keys():
			return PASSAGE[f"{x}{y}"]
		return (x,y)
		
	moves = get_move(x,y)
	print(f"\nMoves: {moves}")
	
	moves = [move for move in moves if is_valid(move[0], move[1]) and not reverse_move(move[0], move[1])]
	print(f"\nMoves: {moves}")
	
	moves = [tunnel(move[0], move[1]) for move in moves]
	print(f"\nMoves: {moves}")
	
	return moves
	
	
def exit(x,y)->bool:
	if (x,y) in EXIT:
		return True
	return False	
		

def solve(X):

	STACK.append(Solution([X]))
	
	for _ in range(3):
		X = STACK.pop(-1)
		
		x, y = X.path[-1][0], X.path[-1][1]
		print(f"\n\nPosition: {x}, {y}")
		
		moves = next_move(x,y)
		
		# WARNING ! check last move - reverse move
		
		# check if EXIT is in next move
		for move in moves:
			if exit(move[0], move[1]):
				# solution found
				return 0
					
		# Case - if the Frog is stuck ??
			
		# Stack - define new plateau (position)
		for move in moves:
			y = Solution(X.path+[move])
			STACK.append(y)
		
		print("\n")
		for stack in STACK:
			print(stack.path)
		input()

if __name__ == "__main__":
	
	solve(FROG)
	
	
	
