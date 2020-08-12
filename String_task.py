n = input()
str = ['a','e','i','o','u','y','A','E','I','O','U','Y']
for i in n:
    if i in str:
        n = n.replace(i,'')
n = n.lower()
print('.'+'.'.join(n))
