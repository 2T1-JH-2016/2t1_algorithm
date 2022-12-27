import sys; input = sys.stdin.readline
m, n = map(int,input().split())
np = dict()

for inx in range(m) :
    p = input().strip()
    np[p] = (inx+1)
    np[str(inx+1)] = p

for _ in range(n) :
    p = str(input().strip())
    print(np[p])