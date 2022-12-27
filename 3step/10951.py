# 주의할 점 : 더이상 읽을 데이터가 없으면 종료
import sys
try :
    while True :
        a,b=map(int,sys.stdin.readline().split())
        print(a+b)
except:
    exit()
