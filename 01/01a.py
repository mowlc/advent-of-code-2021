data = open("data01", "r")
field = [int(x) for x in data.readlines()] 
prev = field[0] + field[1] + field[2]
co = 0
for i in range(len(field) - 2):
	if prev < field[i] + field[i + 1] + field[i + 2]:
		co += 1
	prev = field[i] + field[i + 1] + field[i + 2]
print(co)
	