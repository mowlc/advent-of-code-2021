def make_flash(i, j):
	global flashes
	global grid
	global current_flashes
	if (i,j) not in current_flashes:
		flashes += 1
		current_flashes.append((i,j))
		if 0 <= i - 1 < len(grid):
			grid[i - 1][j] += 1
			if grid[i - 1][j] > 9:
				make_flash(i - 1,j)
		if 0 <= i + 1 < len(grid):
			grid[i + 1][j] += 1
			if grid[i + 1][j] > 9:
				make_flash(i + 1,j)
		if 0 <= j - 1 < len(grid[i]):
			grid[i][j - 1] += 1
			if grid[i][j - 1] > 9:
				make_flash(i,j - 1)
		if 0 <= j + 1 < len(grid[i]):
			grid[i][j + 1] += 1
			if grid[i][j + 1] > 9:
				make_flash(i,j + 1)
		if 0 <= i - 1 < len(grid) and 0 <= j - 1 < len(grid[i]):
			grid[i - 1][j - 1] += 1
			if grid[i - 1][j - 1] > 9:
				make_flash(i - 1,j - 1)
		if 0 <= i - 1 < len(grid) and 0 <= j + 1 < len(grid[i]):
			grid[i - 1][j + 1] += 1
			if grid[i - 1][j + 1] > 9:
				make_flash(i - 1,j + 1)
		if 0 <= i + 1 < len(grid) and 0 <= j - 1 < len(grid[i]):
			grid[i + 1][j - 1] += 1
			if grid[i + 1][j - 1] > 9:
				make_flash(i + 1,j - 1)
		if 0 <= i + 1 < len(grid) and 0 <= j + 1 < len(grid[i]):
			grid[i + 1][j + 1] += 1
			if grid[i + 1][j + 1] > 9:
				make_flash(i + 1,j + 1)

flashes = 0
grid = [[int(a) for a in d.strip()] for d in open("data", "r").readlines()]
current_flashes = []

for _ in range(100):
	for i, row in enumerate(grid):
		for j, col in enumerate(row):
			grid[i][j] += 1
			if grid[i][j] > 9:
				make_flash(i, j)
	for i,j in current_flashes:
		grid[i][j] = 0
	current_flashes = []


		

print(flashes)
		
