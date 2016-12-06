pad = [[1,2,3],[4,5,6],[7,8,9]]

#x = [x for x in pad if 3 in x][0]
#print 'The index is (%d,%d)' %( pad.index(x), x.index(3) )
def moving(x, y, input):
	for move in input:
		if move == 'R':
			y += 1 if y < 2 else 0			
		elif move == 'L':
			y -= 1 if y > 0 else 0
		elif move == 'U':
			x -= 1 if x > 0 else 0
		elif move == 'D':
			x += 1 if x < 2 else 0
	return [x,y]

def getNumber(coor):
	return pad[coor[0]][coor[1]]


with open('day2_input.txt') as f:
    content = f.readlines()		

result = []
x = 1
y = 1
for input in content:
	coor = moving(x, y, input)
	x = coor[0]
	y = coor[1]
	result.append(getNumber(coor))
print result