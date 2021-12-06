data = open("data", "r").readline().strip()
data = [int(x) for x in data.split(",")]

fish_age = [0 for _ in range(10)]

for d in data:
	fish_age[d] += 1

for day in range(256):
	for f in range(len(fish_age)):
		if f == 0:
			fish_age[7] += 1 * fish_age[f]
			fish_age[9] += 1 * fish_age[f]
			fish_age[f] = 0
		else:
			fish_age[f-1] += 1 * fish_age[f]
			fish_age[f] = 0

print(sum(fish_age))