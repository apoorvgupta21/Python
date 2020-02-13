# Problem Statement: In an array l[], find the highest number and give the difference with the lowest number left to it in an array.

l = [2, 3, 10, 6, 4, 8, 1]
max = max(l)
print("Max of list is=", max)
i = 0
lnew = []
print("List of 1st element is", l[i])
while((l[i] < max )):
	print ("I am here")	
	lnew.insert(i, l[i])    # insert/append l[i] at i position in empty array lnew[]
	i = i + 1
	print(lnew)

min = min(lnew)
val = max - min
print ("Value is =", val)		
