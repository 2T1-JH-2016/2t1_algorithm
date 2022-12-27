# A, B 길이 짧은 것 우선
# A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저
# 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.

import re
from operator import attrgetter

class NumberData:
    def __init__(self, code):
        self.length = len(code)
        self.code = code
        self.nums = sum(map(int,re.findall("\d", code)))
    def print(self):
        print(self.code)

n = int(input())
n_list = list()

for _ in range(0,n) : 
    code = input()
    n_list.append(NumberData(code))


sorted_list = sorted(n_list, key= attrgetter('code'))
sorted_list = sorted(sorted_list, key= attrgetter('nums'))
sorted_list = sorted(sorted_list, key= attrgetter('length'))


for item in sorted_list : 
    item.print()