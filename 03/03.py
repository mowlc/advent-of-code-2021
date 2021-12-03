data = open("data03", "r")
field = [ x.strip() for x in data.readlines()]
print(field)

common = [0 for _ in range(len(field[0]))]

gamma = ""
epsilon = ""

for f in field:
	for b in range(len(f)):
		common[b] += int(f[b])

for i in common:
	if i > len(field) / 2:
		gamma += "1"
		epsilon += "0"
	else:
		gamma += "0"
		epsilon += "1"

gamma_i = eval('0b' + gamma)
epsilon_i = eval('0b' + epsilon)
print(gamma_i * epsilon_i)

