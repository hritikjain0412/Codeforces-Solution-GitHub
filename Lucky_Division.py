
n = int(input())
x = str(n)
y = "74"
count = 0
v = True
for i in range(len(x)):
    if x[i] == y[0] or x[i] == y[1]:
        count += 1
if count == len(x):
    v= False
    print("YES")
if v == True:
    if n%7==0 or n%4 == 0:
        print("YES")
    else:
        print('NO')

'''
#your code goes here

n = input()
count = 0
#for i in range(len(n)-2):
i = 0
while(i<len(n)-2):
    if n[i]=="A":
        if n[i+1]=="B":
            if n[i+2]=="C":
                count += 1
        elif n[i+1]=="C":
            if n[i+2] == "B":
                count += 1

    elif n[i]=="B":
        if n[i+1]=="A":
            if n[i+2]=="C":
                count += 1
                print("hi",count)
        elif n[i+1]=="C":
            if n[i+2] == "A":
                count += 1

    elif n[i]=="C":
        if n[i+1]=="B":
            if n[i+2]=="A":
                count += 1
        elif n[i+1]=="A":
            if n[i+2] == "B":
                count += 1
    i = i + 1
print(count)
'''
