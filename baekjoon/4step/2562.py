import sys; input = sys.stdin.readline
n_list = [int(input()) for _ in range(9)]
m = max(n_list)
print(m)
print(n_list.index(m)+1)