#    Main Author(s): Jurgen Bueno, Seyed Iman Modarres Sadeghi
#    Main Reviewer(s):

from a1_partc import Queue

def get_overflow_list(grid):
	'''
	Return the coordinates of cells that will overflow.

		Parameters:
			grid (list): a 2D array representing a grid
		
		Returns:
			resized_overflow_cells (list): a list of cells that will overflow
									if empty, will return None
	'''
	length = len(grid)
	width = len(grid[0])

	overflow_cells = Queue()

	for i in range(length):
		for j in range(width):

			# get the absolute value of the cell value
			if grid[i][j] < 0:
				cell_value = grid[i][j] * -1
			else:
				cell_value = grid[i][j]
			
			# check all directions for neighbours
			num_neighbours = 0

			if i - 1 >= 0: # check up
				num_neighbours += 1

			if i + 1 < length: # check down
				num_neighbours += 1

			if j - 1 >= 0: # check left
				num_neighbours += 1

			if j + 1 < width: # check right
				num_neighbours += 1

			if cell_value >= num_neighbours:
				overflow_cells.enqueue((i, j))

	if (len(overflow_cells) != 0):
		# print("{}".format(len(overflow_cells)))
		# print(len(overflow_cells) == 0.3)
		# resize the list to match number of overflowed cells
		resized_overflow_cells = Queue(len(overflow_cells))

		for i in range(len(overflow_cells)):
			resized_overflow_cells.enqueue(overflow_cells.dequeue())
			
		# print("{}, {}".format(len(overflow_cells), len(resized_overflow_cells)))
		return resized_overflow_cells.list #returns the resized list (so it takes (2) from.)
		# return overflow_cells.list

	return None


def overflow(grid, a_queue):
	'''
	Return the number intermediate grids created while grid was overflowing

		Parameters:
			grid (list): a 2D array representing a grid
			a_queue (Queue): an instance of Queue
		
		Returns:
			grids_added (int): a number representing the number of grids added to a_queue
	'''

	def overflow_recursive(grid, a_queue, grids_added = 0):
		noOfRows = len(grid)
		noOfCols = len(grid[0])

		overflowList = get_overflow_list(grid)

		areAllSameSign = True
		temp = None
		for i in range(noOfRows):
			for j in range(noOfCols):
				if(grid[i][j] != 0):
					if(temp == None):
						temp = grid[i][j]
					else:
						if(grid[i][j] * temp < 0):
							areAllSameSign = False
							break

		if(overflowList == None or areAllSameSign):
			return grids_added

		sign = grid[overflowList[0][0]][overflowList[0][1]] > 0
		
		for cell in overflowList:
			row = cell[0]
			col = cell[1]

			grid[row][col] = 0

		for cell in overflowList:
			row = cell[0]
			col = cell[1]

			value = 1 if sign else -1

			if(col + 1 < noOfCols):
				if((grid[row][col + 1] > 0 and sign == False) or (grid[row][col + 1] < 0 and sign == True)):
					grid[row][col + 1] *= -1
				grid[row][col + 1] += value

			if(col - 1 >= 0):
				if((grid[row][col - 1] > 0 and sign == False) or (grid[row][col - 1] < 0 and sign == True)):
					grid[row][col - 1] *= -1
				grid[row][col - 1] += value

			if(row + 1 < noOfRows):
				if((grid[row + 1][col] > 0 and sign == False) or (grid[row + 1][col] < 0 and sign == True)):
					grid[row + 1][col] *= -1
				grid[row + 1][col] += value

			if(row - 1 >= 0):
				if((grid[row - 1][col] > 0 and sign == False) or (grid[row - 1][col] < 0 and sign == True)):
					grid[row - 1][col] *= -1
				grid[row - 1][col] += value

		
		newGrid = [None] * noOfRows
		for i in range(noOfRows):
			newGrid[i] = [None] * noOfCols

		for i in range(noOfRows):
			for j in range(noOfCols):
				newGrid[i][j] = grid[i][j] 
		
		a_queue.enqueue(newGrid)

		return overflow_recursive(grid, a_queue, grids_added + 1)
	
	return overflow_recursive(grid, a_queue)
