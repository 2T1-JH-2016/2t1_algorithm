n = input().zfill(2)
n_list = list(n)
cnt = 0
while True :
    a = list(str(int(n_list[0]) + int(n_list[1])).zfill(2))
    n_list[0],n_list[1] = n_list[1],a[1]
    cnt += 1
    if(n_list == list(n)):
        print(cnt)
        break