def countEvens(theList):
	n = 0
	for i in theList:
		if i % 2 == 0:
			n = n + 1
	return n


print countEvens([2,1,2,3,4])#3
print countEvens([2,2,0])#3
print countEvens([1,3,5])#0

def bigDiff(List):

	max = List[0]

	for x in List:
		if x > max:
			max = x

	min = List[0]

	for a in List:
		if a < min:
			min = a

	return max - min

print bigDiff([10, 3, 5, 6])# 7
print bigDiff([7, 2, 10, 9])# 8
print bigDiff([2, 10, 7, 2])# 8

#def centerdAverage(lista):
	



#print centeredAverage([1, 2, 3, 4, 100])#3
#print centeredAverage([1, 1, 5, 5, 10, 8, 7])#5
#print centeredAverage([-10, -4, -2, -4, -2, 0])#-3