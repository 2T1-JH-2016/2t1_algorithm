def findSelfNumber(a) :
    n = a + sum(map(int,list(str(a))))

    if(n < 10001 and n_list[n] == 1) :
        n_list[n] = 0
        findSelfNumber(n)

n_list = [1] * 10001

for i in range(len(n_list)) : 
    findSelfNumber(i)

for i in range(len(n_list)) : 
    if( n_list[i] == 1) :
        print(i)
