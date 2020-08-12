a,b = map(int,input().split())
num = list(map(int,input().split()))
arr = []
for i in range(a):
    if num[i]>=num[b-1] and num[i]>0:
        arr.append(num[i])
print(len(arr))
