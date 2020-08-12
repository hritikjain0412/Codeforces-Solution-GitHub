n = input()
v = True

for i in range(len(n)):
    if n[i] == 'H':
        print('YES')
        v = False
        break
    elif n[i] == 'Q':
        print('YES')
        v = False
        break
    elif n[i] == '9':
        print('YES')
        v = False
        break
    elif n[i] == '+':
        print('YES')
        v = False
        break
if v:
    print("NO")
