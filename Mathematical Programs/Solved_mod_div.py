"""if __name__ == '__main__':
    n = int(input())
    i = 0
    temp = 0
    for i in range(i,n):
        temp = temp + n*(pow(10,i))        
        i = i+1
        n = n-1
    print(temp)"""

if __name__ == '__main__':
    n = int(input())
    print(*range(1, n + 1), sep='')