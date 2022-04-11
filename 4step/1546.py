def newMid(score) :
    return score/mx*100

cnt = int(input())
n = list(map(int,input().split()))

mx = max(n)
n_list = []

for i in n:
    n_list.append(newMid(i))

print(sum(n_list)/cnt)