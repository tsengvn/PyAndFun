import math
def test(array) :
	startX = 0
	startY = 0
	destX = startX
	destY = startY

	face = 'N'
	for input in array:
		input = input.strip()
		direction = input[0]
		step = int(input[1:])
		if direction == 'R' and face == 'N':
			destX += step
			face = 'E'
		elif direction == 'R' and face == 'W':
			destY += step
			face = 'N'
		elif direction == 'R' and face == 'E':
			destY -= step
			face = 'S'
		elif direction == 'R' and face == 'S':
			destX -= step
			face = 'W'
		elif direction == 'L' and face == 'N':
			destX -= step
			face = 'W'
		elif direction == 'L' and face == 'W':
			destY -= step
			face = 'S'
		elif direction == 'L' and face == 'E':
			destY += step
			face = 'N'
		elif direction == 'L' and face == 'S':
			destX += step
			face = 'E'
		#print "dest(%s %s)" %(destX, destY)
	print "start(%s %s)" %(startX, startY)		
	print "dest(%s %s)" %(destX, destY)
	distance = math.fabs(startX - destX) + math.fabs(startY - destY)
	print distance

input = "L1, L3, L5, L3, R1, L4, L5, R1, R3, L5, R1, L3, L2, L3, R2, R2, L3, L3, R1, L2, R1, L3, L2, R4, R2, L5, R4, L5, R4, L2, R3, L2, R4, R1, L5, L4, R1, L2, R3, R1, R2, L4, R1, L2, R3, L2, L3, R5, L192, R4, L5, R4, L1, R4, L4, R2, L5, R45, L2, L5, R4, R5, L3, R5, R77, R2, R5, L5, R1, R4, L4, L4, R2, L4, L1, R191, R1, L1, L2, L2, L4, L3, R1, L3, R1, R5, R3, L1, L4, L2, L3, L1, L1, R5, L4, R1, L3, R1, L2, R1, R4, R5, L4, L2, R4, R5, L1, L2, R3, L4, R2, R2, R3, L2, L3, L5, R3, R1, L4, L3, R4, R2, R2, R2, R1, L4, R4, R1, R2, R1, L2, L2, R4, L1, L2, R3, L3, L5, L4, R4, L3, L1, L5, L3, L5, R5, L5, L4, L2, R1, L2, L4, L2, L4, L1, R4, R4, R5, R1, L4, R2, L4, L2, L4, R2, L4, L1, L2, R1, R4, R3, R2, R2, R5, L1, L2"
#input = "R2, R2, R2, R191"
test(input.split(','))