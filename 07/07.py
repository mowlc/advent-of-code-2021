import statistics
data = open("data", "r").readline().strip()

data = [int(x) for x in data.split(",")]

median = sorted(data)[int(len(data) / 2)]

cost = 0
for d in data:
	cost += abs(d - median)

print(cost)
