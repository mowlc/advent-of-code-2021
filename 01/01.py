data = open("data01", "r")
field = [int(x) for x in data.readlines()] 
prev = field[0]
co = 0
for i in range(len(field)):
	if prev < field[i]:
		co += 1
	prev = field[i]
print(co)
	