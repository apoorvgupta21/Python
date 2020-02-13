#Insertion Sort:

def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        currnum = arr[i]                                        # As we are navigating by comparing the 2nd element of list and navigating right to left.
        print(currnum)
        # Move elements of arr[0..i-1], that are 
        # greater than currnum, to one position ahead 
        # of their current position 
        position = i        
        while((position > 0) and (currnum < arr[position-1])):   # Position should always be greater than 0 otherwise we cannot compare and currnum should be less than value in left to swap                
                arr[position] = arr[position-1]
                #print(arr[+1])
                position -= 1  
                #print(j)
        arr[position] = currnum
    
    return(arr)
    

arr = [12, 11, 13, 5, 6] 
a1 = insertionSort(arr) 
print(a1)

