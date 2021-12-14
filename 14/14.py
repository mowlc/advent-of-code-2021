data = open("data", "r").readlines() 

template = data[0].strip()
pairs = {}
for d in data[2:]:
	tmp = d.strip().split(" -> ")
	pairs[tmp[0]] = tmp[1]

for step in range(40):
	tmp = template[0]
	for i in range(len(template) - 1):
		tmp += pairs[template[i:i + 2]] + template[i + 1]
	template = tmp

count = {}
for i in template:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1

print(count[max(count, key=count.get)] - count[min(count, key=count.get)])

