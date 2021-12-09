def find_basin(pos, data, i, j):
	candidates = []
	if 0 <= i - 1 < len(data):
		candidates.append([i - 1, j])
	if 0 <= i + 1 < len(data):
		candidates.append([i + 1, j])
	if 0 <= j - 1 < len(row):
		candidates.append([i, j - 1])
	if 0 <= j + 1 < len(row):
		candidates.append([i, j + 1])
	if len(candidates) == 0:
		if [i, j] not in pos:
			return [i, j]
	else:
		for c in candidates:
			if int(data[c[0]][c[1]]) != 9 and [c[0], c[1]] not in pos:
				pos.append([c[0], c[1]])
				find_basin(pos, data, c[0], c[1])
		return pos


data = [[a for a in d.strip()] for d in open("data", "r").readlines() ]
risk_areas = []
for i, row in enumerate(data):
	for j, col in enumerate(row):
		candidates = []
		if 0 <= i - 1 < len(data):
			candidates.append(int(data[i - 1][j]))
		if 0 <= i + 1 < len(data):
			candidates.append(int(data[i + 1][j]))
		if 0 <= j - 1 < len(row):
			candidates.append(int(data[i][j - 1]))
		if 0 <= j + 1 < len(row):
			candidates.append(int(data[i][j + 1]))
		if min(candidates) > int(col):
			risk_areas.append([i,j])


basins = []
for area in risk_areas:
	basins.append(len(find_basin([area], data, *area)))

basins.sort()
print(basins[-1] * basins[-2] * basins[-3])