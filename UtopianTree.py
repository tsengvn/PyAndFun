import math
import sys

def utopian(cycle):
	mod2 = cycle % 2 == 0
	base = math.ceil(cycle / 2.0)
	result = math.pow(2, base+1) - (1 if mod2 else 2)

	print result

#utopian(float(sys.argv[1]))
utopian(10)