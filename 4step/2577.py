a = int(input())
b = int(input())
c = int(input())

n = list(map(int,str(a * b * c)))
n_dict = dict()

for i in n :
    if(i in n_dict) :
        n_dict[i] += 1
    else :
        n_dict[i] = 1


for i in range(10) :
    if(i in n_dict):
        print(n_dict[i])
    else :
        print(0)