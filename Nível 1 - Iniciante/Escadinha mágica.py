x = int(input())

for y in range(1,x+1):
    for n in range(1,y+1):
        if n == y:
            print(n,end='')
        else:
            print(n,end=' ')
    print()