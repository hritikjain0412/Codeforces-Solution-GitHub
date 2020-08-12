a,b = map(int,input().split())
arr =list(map(int,input().split()))
res = []
for i in range((a-b)+1):
    num = arr[i:b+i]
    val = sum(num)/len(num)
    res.append(val)
res.append(sum(arr)/len(arr))
print(round(max(res),15))
