brackets = {
	"(": ")",
    "{": "}",
    "[": "]",
    "<": ">"
}

scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

data = [[a for a in d.strip()] for d in open("data", "r").readlines() ]

score = []

for case in data:
	stack =[]
	for bracket in case:
		if bracket in brackets:
			stack.append(brackets[bracket])
		elif bracket == stack[-1]:
			stack.pop()
		else:
			stack = []
			break
	stack_score = 0
	for s in stack[::-1]:
		stack_score *= 5
		stack_score += scores[s]
	if stack_score:	
		score.append(stack_score)


print(sorted(score)[int(len(score) / 2)])
