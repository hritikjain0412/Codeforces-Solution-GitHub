from collections import defaultdict
x = int(input())
num = list(map(int,input().split()))
map = defaultdict(int)
for i in range(x):
    map[num[i]] += 1
max_value = max(map.values())
print(map)
print(max_value)
