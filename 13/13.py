def printGrid(grid):
	for g in grid:
		print(g)
data = open("data", "r").readlines() 

points = []
folds = []

st = 0
for i, line in enumerate(data):
	if line.strip() == "":
		st = i + 1
		break
	else:
		points.append([int(x) for x in line.strip().split(",")])

for line in range(st, len(data)):
	folds.append(data[line].strip().split("fold along ")[1].split("="))

for fold in folds:
	new_points = []
	for i, point in enumerate(points):
		new_point = []
		if fold[0] == "x":
			if point[0] > int(fold[1]):
				new_point = [2 * int(fold[1]) - point[0], point[1]]
			else:
				new_point = point
		else:
			if point[1] > int(fold[1]):
				new_point = [point[0], 2 * int(fold[1]) - point[1]]
			else:
				new_point = point
		if new_point not in new_points:
			new_points.append(new_point)

	points = [p for p in new_points]

print(new_points)
max_x = 0
max_y = 0
for p in new_points:
	if p[0] > max_x:
		max_x = p[0]
	if p[1] > max_y:
		max_y = p[1]
grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1	)]
for p in new_points:
	grid[p[1]][p[0]] = "#"
printGrid(grid)
