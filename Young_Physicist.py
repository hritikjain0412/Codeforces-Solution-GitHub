n = int(input())
p = []
q = []
r = []
for i in range(n):
    x,y,z = map(int,input().split())
    p.append(x)
    q.append(y)
    r.append(z)
if sum(p) == sum(q) == sum(r) == 0:
    print("YES")
else:
    print('NO')
