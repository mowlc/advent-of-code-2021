import sys
data = open("data", "r").readline().strip()

data = [int(x) for x in data.split(",")]

optimal = sys.maxsize

for init in range(len(data)):
	cost = 0
	for d in data:
		tmp = abs(d - init)
		cost += (tmp * (tmp + 1)) / 2 
	if optimal > cost:
		optimal = cost
print(optimal)