def checkBoard(board, nums):
	for b in board:
		if set(b).issubset(nums):
			flat = set([item for sublist in board for item in sublist])
			return (True, flat.difference(nums))
	return (False,-1) 


data = open("data", "r")

numbers = [int(x) for x in data.readline().strip().split(",")]
data.readline()

boards = []
curr_board = []
lines = 1
for line in data.readlines():
	if lines % 6 == 0:
		boards.append(curr_board)
		curr_board = []
		lines += 1
	else:
		curr_board.append([int(x) for x in line.strip().split(" ")])
		lines += 1


for b in range(len(boards)):
	for l in list(map(list, zip(*boards[b]))):
		boards[b].append(l)

bingoNums = set()
for num in numbers:
	isBreak = False
	bingoNums.add(num)
	boardNum = 0
	for board in boards:
		tmp = checkBoard(board, bingoNums)
		if tmp[0]:
			if len(boards) == 1:
				print(sum(tmp[1]) * num)
				isBreak = True
				break
			else:
				boards.remove(board)
		boardNum += 1
	if isBreak:
		break
