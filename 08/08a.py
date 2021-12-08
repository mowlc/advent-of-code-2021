"""nums = {
	0: set(["a","b","c","d","e","g"]),
	1: set(["a","b"]),
	2: set(["a","c","d","f","g"]),
	3: set(["a","b","c","d","f"]),
	4: set(["a","b","e","f"]),
	5: set(["b","c","d","e","f"]),
	6: set(["b","c","d","e","f","g"]),
	7: set(["a","b","d"]),
	8: set(["a","b","c","d","e","f","g"]),
	9: set(["a","b","c","d","e","f"])
}"""

data = [d.strip().split(" | ") for d in open("data", "r").readlines()]

inp = [[set([ z for z in y]) for y in x[0].split(" ")] for x in data]

out = [[set([ z for z in y]) for y in x[1].split(" ")] for x in data]

suma = 0
for idx, i in enumerate(inp):
	nums = [set() for _ in range(10)]

	i.sort(key=len)

	nums[1] = i[0]
	nums[7] = i[1]
	nums[4] = i[2]
	nums[8] = i[9]
	nums235 = i[3:6]
	nums069 = i[6:9]

	#NUM 3
	for n in nums235:
		if nums[7].issubset(n):
			nums[3] = n
			break

	#NUM 9
	nums[9] = nums[1].union(nums[3]).union(nums[4])

	#NUM 0
	nums[0] = (nums[8] - nums[3]).union(nums[9]- nums[4]).union(nums[1])

	#NUM 6
	for n in nums069:
		if n != nums[0] and n != nums[9]:
			nums[6] = n

	#NUM 5
	nums[5] = nums[6] - (nums[8] - nums[9])

	#NUM 2
	nums[2] = (nums[8] - nums[5]).union(nums[3] - nums[1])

	out_num = ""
	for o in out[idx]:
		for n in range(len(nums)):
			if o == nums[n]:
				out_num += str(n)
	suma += int(out_num)	

print(suma)



