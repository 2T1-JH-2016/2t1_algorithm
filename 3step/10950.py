count = int(input())
ans = list()
for _ in range(count) :
    a, b = map(int, input().split())
    ans.append(a+b)

for item in ans :
    print(item)