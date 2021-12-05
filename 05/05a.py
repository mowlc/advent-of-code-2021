
def printGrid(grid):
	for l in grid:
		print(l)	

def myRange(a, b):
	if a > b:
		return range(b,a + 1)
	else:
		return range(a,b + 1)

def countOverlap(grid):
	r = 0
	for l in grid:
		for i in l:
			if i > 1:
				r += 1
	return r

data = open("data", "r")

lines = []

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in data.readlines():
	tmp = line.strip().split(" -> ")
	lines.append((tuple(tmp[0].split(",")),tuple(tmp[1].split(","))))

for l in lines:
	#for horizontal and vertial lines
	if l[0][0] == l[1][0]:
		for y in myRange(int(l[0][1]), int(l[1][1])):
			grid[y][int(l[0][0])] += 1
	elif l[0][1] == l[1][1]:
		for x in myRange(int(l[0][0]), int(l[1][0])):
			grid[int(l[0][1])][x] += 1
	#for diagonal lines
	elif int(l[0][0]) < int(l[1][0]):
		if int(l[0][1]) < int(l[1][1]):
			for x in range(int(l[1][0]) - int(l[0][0]) + 1):
				grid[int(l[0][1]) + x][int(l[0][0]) + x] += 1
		else:
			for x in range(int(l[1][0]) - int(l[0][0]) + 1):
				grid[int(l[0][1]) - x][int(l[0][0]) + x] += 1
	else: 
		if int(l[0][1]) < int(l[1][1]):
			for x in range(int(l[0][0]) - int(l[1][0]) + 1):
				grid[int(l[0][1]) + x][int(l[0][0]) - x] += 1
		else:
			for x in range(int(l[0][0]) - int(l[1][0]) + 1):
				grid[int(l[0][1]) - x][int(l[0][0]) - x] += 1

print(countOverlap(grid))
