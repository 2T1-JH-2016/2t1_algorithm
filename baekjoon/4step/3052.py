n_list = dict()
for _ in range(10):
    n = int(input())%42
    if(n in n_list) :
        n_list[n] += 1
    else : 
        n_list[n] = 1


print(len(n_list))