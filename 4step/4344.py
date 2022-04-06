for _ in range(int(input())) :
    a = list(map(int,input().split()))
    m = sum(a[1:])/a[0]
    cnt = 0
    for i in range(1,len(a)) :
        if(a[i] > m) :
            cnt += 1
    print("{:.3f}%".format(cnt/a[0]*100))
