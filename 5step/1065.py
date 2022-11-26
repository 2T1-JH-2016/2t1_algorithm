def checkHan(_list) :
    a = _list[1] - _list[0]
    for i in range(1,len(_list)-1) :
        if a != _list[i+1] - _list[i] :
            return False
    return True

n = int(input())


if(n < 100) :
    print(n)
else :
    cnt = 99
    for j in range(100,n+1) :
        n_list = list(map(int,list(str(j))))
        if checkHan(n_list) :
            cnt += 1

    print(cnt)