n = int(input())
num = list(map(int,input().split()))
num.sort(reverse = True)
#print(num)
total = sum(num)/2
#print(total)
count = 1
res = num[0]
for i in range(n):
    if res>total:
        print(count)
        break
    else:
        res = res + num[i+1]
        count += 1
