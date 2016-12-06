with open('day3_input.txt') as f:
    text = f.readlines()		

#input = [[1,2,5], [5,1,9], [6,7,4]]

result = 0
for input in text:
	input = input.split()
	input = list(map(int, input))

	input.sort()
	print input
	result += 1 if input[2] < (input[0] + input[1]) else 0

print result	