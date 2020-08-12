n = int(input())
count = 0
for i in range(n):
    x,y,z = map(int,input().split())
    if x==y==1 or x==z==1 or y==z==1:
        count += 1
print(count)
