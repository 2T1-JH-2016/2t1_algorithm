import sys; input = sys.stdin.readline
a, x = map(int,input().split())
visit = list(map(int,input().split()))

if(max(visit)):
    cnt = 1
    mx = res = sum(visit[:x])
    for i in range(x,a):
        res += visit[i]-visit[i-x]
        if res > mx :
            mx = res
            cnt = 1
        elif res == mx : 
            cnt += 1
    print(mx,cnt,sep='\n')
else :
    print("SAD")