import math
num = list(map(int,input().split()))
a = math.ceil(num[0]/num[2])
b = math.ceil(num[1]/num[2])
print(a*b)
