# Bubble Sort Program: 
# Algo
# Compare the first two element of an array, if arr[0] < arr[1], ignore otherwise swap them. 

a = [4, 9, 2, 3, 38, 22, 83, 19, 76, 5, 1, 45]
l = len(a)
print(l)
i = 0
j = 0
temp = 0

#for j in range(j, l-1):
while(j < l):
	i = 0
	for i in range(i, l-1):
		if(a[i] < a[i+1]):
			i = i + 1
			pass
		else:
			temp = a[i+1]
			a[i+1] = a[i]
			a[i] = temp
			i = i + 1
	j = j+1

print(a)


