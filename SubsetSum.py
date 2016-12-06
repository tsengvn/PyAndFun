#Detect if a subset from a given set of N non-negative integers sums upto a given value S.
#Example: 
#Set: {1, 3, 9, 2}, S = 5
#Output: true

def detect(S, array) :
	if len(array) == 0:
		return 0

	result = 0
	length = len(array)
	
	for i in xrange(0, length):	
		check = []
		check.append(array[i])
		step = 1
		lastAppend = 0
		while lastAppend < length:
			for j in xrange(i+step, length):
				currentSum = sum(check, array[j])
				if currentSum < S:
					check.append(array[j])
					lastAppend = j
					print check
				elif currentSum == S:
					result += 1
					check.append(array[j])
					print check
					break
				
			step += 1
			if i + step >= length: 
				break

	return result	

print detect(53, [15, 22, 14, 26, 32, 9, 16, 8]) #3
#print detect(11, [1, 3, 9 ,5, 1]) #1
#print detect(9, [3, 34, 4, 12, 5, 2]) #1
#print detect(53, [15, 22 ,14,26, 32 ,9, 16, 8]) #3
#print detect(5842, [267, 493, 869, 961,1000,1153,1246,1598,1766,1922]) #1
#print detect(50, [41,34,21,20, 8, 7, 7, 4, 3, 3]) #1
#print detect(10, [25,27, 3,12, 6,15, 9,30,21,19]) #1
#print detect(4, [4]) #1
#print detect(12, [4, 8, 10, 12]) #2
#print detect(30, [1,2,3,4,5,6]) #0



