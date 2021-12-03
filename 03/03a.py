def eliminateNonDominant(whole,i):
	co = 0
	for l in whole:
		co += int(l[i])
	dominant = "1" if co >= len(whole) / 2 else "0"
	return [f for f in whole if f[i] == dominant]

def eliminateDominant(whole,i):
	co = 0
	for l in whole:
		co += int(l[i])
	dominant = "1" if co < len(whole) / 2 else "0"
	return [f for f in whole if f[i] == dominant]

def getOxygen(list, index):
	if len(list) == 1:
		return eval('0b' + list[0])
	return getOxygen(eliminateNonDominant(list, index + 1), index + 1)

def getCO2(list, index):
	if len(list) == 1:
		return eval('0b' + list[0])
	return getCO2(eliminateDominant(list, index + 1), index + 1)


data = open("data03", "r")
field = [ x.strip() for x in data.readlines()]

print(getOxygen(field, -1) * getCO2(field, -1))