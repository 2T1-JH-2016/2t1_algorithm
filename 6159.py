# S(1 <= S <= 1,000,000)
# N(2 <= N <= 20,000)
# 소i의 사이즈는 (1 <= L_i <= 1,000,000)
# 소 두마리의 크기 합이 코스튬의 크기 이하인 경우 둘이 코스튬에 들어갈 수 있음
# 4 6
#3
#5
#2
#1
import sys; input = sys.stdin.readline

n, s = map(int,input().split())
n_list = list()
for _ in range(n) :
    n_list.append(int(input()))

cnt = 0
start = 0
end = n-1

n_list.sort()

while(start < end) :
    if n_list[start] + n_list[end] > s :
        end -= 1
    else :
        cnt += end - start
        start += 1
print(cnt)