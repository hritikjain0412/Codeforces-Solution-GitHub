x = int(input())
arr = []
for i in range(x):
    y = input()
    arr.append(y)
for i in range(x):
    n = arr[i]
    length = len(n)
    if length>10:
        a = n[0]
        b = n[length-1]
        finlen = str(length-2)
        res = a + finlen + b
        print(res)
    else:
        print(arr[i])
