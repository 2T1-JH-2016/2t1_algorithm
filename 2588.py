A = int(input())
B = list(map(int,input()))
sum_num = 0
for idx, n in enumerate(reversed(B)) :
    result = A*n
    print(result)
    sum_num += result * (10**idx)
print(sum_num)