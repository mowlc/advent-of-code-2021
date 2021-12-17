def calc_cost(path):
	cost = 0
	for p in path:
		cost += data[p[1]][p[0]]
	return cost

def find_path(x, y, visited):
	if x == len(data[0]) - 1 and y == len(data) - 1:
		return [[x, y]]
	else:
		paths = []
		if x + 1 < len(data[0]) and [x, y] not in visited:
			paths.append(find_path(x + 1, y, visited + [[x, y]]) + [[x, y]])
		if y + 1 < len(data) and [x, y] not in visited:
			paths.append(find_path(x, y + 1, visited + [[x, y]]) + [[x, y]])
		if x - 1 >= 0 and [x, y] not in visited:
			paths.append(find_path(x - 1, y, visited + [[x, y]]) + [[x, y]])
		if y - 1 >= 0 and [x, y] not in visited:
			paths.append(find_path(x, y - 1, visited + [[x, y]]) + [[x, y]])
		cost = 1000000000
		r_path = []
		for path in paths:
			if [len(data[0]) - 1, len(data) - 1] in path:
				c_cost = calc_cost(path)
				if c_cost < cost:
					cost = c_cost
					print(cost)
					r_path = path
		return r_path


data = [[int(a) for a in d.strip()] for d in open("data", "r").readlines() ]

data2 = [[0] * len(d) * 5 for d in data * 5]

rl = len(data)
cl = len(data[0])

for i in range(len(data2)):
    for j in range(len(data2[i])):
        data2[i][j] = ((data[i % rl][j % cl] + i // rl + j // cl) - 1)  % 9 + 1


data = data2


solve = [[0, 0, 0]]
visited = [[0, 0]]

max_x = len(data[0]) - 1
max_y = len(data) - 1
while len(solve):
	solve.sort(key=lambda x: int(x[2]))
	current = solve.pop(0)
	if current[0] == max_x and current[1] == max_y:
		print(current[2])
		break

	if current[0] + 1 < len(data[0]) and [current[0] + 1, current[1]] not in visited:
		visited.append([current[0] + 1, current[1]])
		solve.append([current[0] + 1, current[1], current[2] + data[current[0] + 1][current[1]]])
	if current[1] + 1 < len(data) and [current[0], current[1] + 1] not in visited:
		visited.append([current[0], current[1] + 1])
		solve.append([current[0], current[1] + 1, current[2] + data[current[0]][current[1] + 1]])
	if current[0] - 1 >= 0 and [current[0] - 1, current[1]] not in visited:
		visited.append([current[0] - 1, current[1]])
		solve.append([current[0] - 1, current[1], current[2] + data[current[0] - 1][current[1]]])
	if current[1] - 1 >= 0 and [current[0], current[1] - 1] not in visited:
		visited.append([current[0], current[1] - 1])
		solve.append([current[0], current[1] - 1, current[2] + data[current[0]][current[1] - 1]])


