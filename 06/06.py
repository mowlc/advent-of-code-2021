data = open("data", "r").readline().strip()
data = [int(x) for x in data.split(",")]

for day in range(256):
	print(day)
	tmp = range(len(data))
	for i in tmp:
		if data[i] == 0:
			data[i] = 7
			data.append(8)
		data[i] -= 1
		
print(len(data))
