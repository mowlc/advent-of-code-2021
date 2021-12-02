def splitF(s):
	return s.split(" ")

data = open("data02", "r")
field = list(map(splitF,[ x.strip() for x in data.readlines()] ))

depth = 0
distance = 0
aim = 0
for command, dist in field:
	if command == 'forward':
		distance += int(dist)
		depth += int(dist) * aim
	elif command == 'down':
		aim += int(dist)
	elif command == 'up':
		aim -= int(dist)
print(depth)
print(distance)
print(aim)
print(depth * distance)
