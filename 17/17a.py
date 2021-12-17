data = open("data", "r").readline().split(": ")[1].split(", ")

x = data[0].split("=")[1].split("..")
y = data[1].split("=")[1].split("..")
x[0] = int(x[0])
x[1] = int(x[1])
y[0] = int(y[0])
y[1] = int(y[1])

c = 0

for i in range(0, 230):
	for j in range(-130, 500):
		cx = 0
		cy = 0

		vi = i
		vj = j

		while True:
			print(c)
			if 0 <= cx <= 230 and -130 <= cy <= 7500:
				cx += vi
				cy += vj

				

				vj -= 1
				if vi:
					vi = vi + (1 if vi < 0 else -1)
			

				if x[0] <= cx <= x[1] and y[0] <= cy <= y[1]:
					c += 1
					break
			else:
				break
print(c)

