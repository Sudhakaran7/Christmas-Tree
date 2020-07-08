def Leaf(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end=' ')
        for k in range(2*i+1):
            print('*',end=' ')
        print()
def bark_pole(n):
    for i in range(n):
        for j in range(n-1):
            print(' ', end=' ')
        print('* * *')
row = int(input())
Leaf(row)
Leaf(row)
bark_pole(row)
