################## Un-Solved #########################
def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
'''
def findx_y(l,r):
    x = 0
    y = 0
    for i in range(l,r+1):
        if l<=i<=r:
            x = i
            break
    for j in range(x+1,r+1):
        if l<=x<j<=r:
            y= j
            break
    lcm = (x*y)//gcd(x,y)
    if l<=lcm<=r:
        return x,y
    else:
        return findx_y(l,r)
'''
n = int(input())
for i in range(n):
    l,r = map(int,input().split())
    x = 0
    y = 0
    for i in range(l,r+1):
        if l<=i<=r:
            x = i
            for j in range(x+1,r+1):
                if l<=x<j<=r:
                    y= j
        lcm = (x*y)//gcd(x,y)
        if l<=lcm<=r:
            print(x,y)
            break
        else:
            continue
