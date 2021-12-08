data = [d.strip().split(" | ") for d in open("data", "r").readlines()]
print(data)

inp = [[len(y) for y in x[0].split(" ")] for x in data]

out = [[len(y) for y in x[1].split(" ")] for x in data]

print(inp)
print(out)
suma = 0
for o in out:
	for i in o:
		if i in [2, 3, 4, 7]:
			suma += 1



print(suma)
