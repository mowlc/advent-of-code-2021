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
			risk_areas.append(int(col) + 1)

print(sum(risk_areas))
		


