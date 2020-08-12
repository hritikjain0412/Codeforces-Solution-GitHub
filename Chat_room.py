def cmp(str):
    s1 = 'hello'
    index = 0

    for i in range(len(str)):
        if index == 5:
            return 'YES'
        if str[i]==s1[index]:
            index += 1

    if index == 5:
        return 'YES'
    else:
        return 'NO'
str = input()
print(cmp(str))




'''
max = 26

def cmp_str(s1,s2):
    flag = False
    v = [0] * max
    for i in range(len(s1)):
        v[ord(s1[i])-ord('a')] = True

    for j in range(len(s2)):
        if v[ord(s2[j])- ord('a')]:
            flag = True

        else:
            flag = False
            break
    return flag
s1 = input()
s2 = 'hello'
V = 0
if len(s1)>5:

    if cmp_str(s1,s2):
        print('YES')
        V = 1
    else:
        print('NO')
        V = 1
if V == 0:
    print("NO")
'''
