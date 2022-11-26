nums = dict()
for i in map(int,input().split()) :
    if i in nums : 
        nums[i] += 1
    else : 
        nums[i] = 1

nums = dict(sorted(nums.items(),reverse=True))
if len(nums) == 1 :
    print(10000 + (max(nums,key=nums.get) * 1000))
elif len(nums) == 2 :
    print(1000 + (max(nums,key=nums.get) * 100))
else :
    print((max(nums,key=nums.get) * 100))