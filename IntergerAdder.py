def add(arr1, arr2):
	
	#print "arr1 %s , arr2 %s" % (arr1, arr2)
	length = len(arr1) if len(arr1) > len(arr2) else len(arr2)
	extra = 0
	result = []
	for x in range(1, length+1):
		index1 = len(arr1) - x
		index2 = len(arr2) - x
		total = extra;

		total += getValue(index1, arr1) + getValue(index2, arr2)
		#total += arr1[index1] if index1 >= 0 else 0
		#total += arr2[index2] if index2 >= 0 else 0
		if total >= 10:
			extra = 1
			total -= 10
		else :
			extra = 0

		result.append(total)

	result.reverse()
	print result

def addComplex(*arrs):
	length = 0
	for arr in arrs:
		length = len(arr) if length < len(arr) else length

	extra = 0
	result = []
	for x in range(1, length+1):
		total = extra
		for arr in arrs:
			index = len(arr) - x
			total += getValue(index, arr)
		if total >= 10:
			extra = total / 10
			total = total % 10
		else :
			extra = 0

		result.append(total)

	result.reverse()
	print result

def getValue(index, array):
	return array[index] if index >= 0 else 0

#add([1,9], [1,2,3])
addComplex([1,9], [1,2,3], [1])