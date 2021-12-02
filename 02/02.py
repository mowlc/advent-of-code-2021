def splitF(s):
	return s.split(" ")

data = open("data02", "r")
field = list(map(splitF,[ x.strip() for x in data.readlines()] ))

depth = 0
distance = 0

for command, dist in field:
	if command == 'forward':
		distance += int(dist)
	elif command == 'down':
		depth += int(dist)
	elif command == 'up':
		depth -= int(dist)
print(depth)
print(distance)
print(depth * distance)
