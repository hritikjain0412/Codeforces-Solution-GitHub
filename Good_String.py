from collections import defaultdict
myMap = defaultdict(int)
n = int(input())
for i in range(n):
    m = input()
    for j in range(len(m)):
        x = int(m[j])
        myMap[x] += 1
    '''
    value = myMap.values()
    max_v=max(value)
    print(max_v)
    '''
    max_key = max(myMap,key = myMap.get)
    print(max_key)
    print(myMap)
