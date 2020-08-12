n = int(input())

while(n>0):
    count = 0
    x = int(input())
    num = list(map(int,input().split()))
    for i in range(x-2):
        if num[i]<num[i+1]>num[i+2]:
            print('YES')
            print(i+1,i+2,i+3)
            count = 1
            break

    if count == 0:
        print("NO")
    n -= 1
