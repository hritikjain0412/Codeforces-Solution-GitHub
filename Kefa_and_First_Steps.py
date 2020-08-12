n = int(input())
num = list(map(int,input().split()))
count = 0
high = 0
for i in range(n-1):
    if num[i]<=num[i+1]:
        count += 1
        if high<count:
             high = count
    else:
        count = 0
print(high+1)
