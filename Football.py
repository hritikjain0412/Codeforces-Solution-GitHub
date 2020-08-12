n = input()
count = 1
v = True
for i in range(len(n)-1):
    if n[i+1] == n[i]:
        count += 1
    else:
        count = 1
    if count >= 7 :
        print('YES')
        v = False
        break

if(v):
    print('NO')
