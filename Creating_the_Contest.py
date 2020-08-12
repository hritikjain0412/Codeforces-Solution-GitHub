n = int(input())
num = list(map(int,input().split()))
#res = []
#for i in range(n):
i = 0
count = 1
j = 1
res = 0
while(j<n):
    if num[j] <= (2*num[i]):
        count += 1


        if j == n-1:
            if res<count:
                res = count
            j += 1

        else:
            j += 1

    else:
        if res<count:
            res = count
        i = i + 1
        j = i+1
        count = 1

#print(res)
print(res)
