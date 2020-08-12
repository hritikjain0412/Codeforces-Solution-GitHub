a,k = map(int,input().split())
main = list(map(int,input().split()))
p = []
q = []
count = 0
for i in range(a):
    if main[i]>k:
        p = main[:i]
        break
    else:
        count += 1
for i in range(a-1,-1,-1):
    if main[i]>k:
        q = main[i+1:]
        break
res = p + q
if len(res) == 0:
    print(count)
else:
    print(len(res))
