def find_way(conns, node, history, path):
	if node == "end":
		return 1
	else:
		ways = 0
		for c in conns[node]:
			if c not in history:
				if c.islower():
					ways += find_way(conns, c, history + [c], path + [node])
				else:
					ways += find_way(conns, c, history, path + [node])

		return ways


paths = [set(d.strip().split("-")) for d in open("data", "r").readlines()]

conns = {}

for a,b in paths:
	if a in conns:
		conns[a] = conns[a] + [b]
	else:
		conns[a] = [b]
	if b in conns:
		conns[b] = conns[b] + [a]
	else:
		conns[b] = [a]


print(find_way(conns, "start", ["start"],[]))

