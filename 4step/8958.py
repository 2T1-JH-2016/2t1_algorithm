n = int(input())

for _ in range(n) : 
    ox = list(input())
    cnt = 0
    score = 0
    for i in ox :
        if(i == 'O') :
            cnt += 1
        else :
            cnt = 0
        score += cnt
    print(score)