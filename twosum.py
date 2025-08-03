num = [10,2,3,5]
target  = 15

seen = {}

def twoSum(num,target):
    print("hello")
    for i in range(0,len(num)):
        compliment = target - num[i]
        if compliment in seen:
             print([seen[compliment],i])
        seen[num[i]] = i

    

twoSum(num,target)
print(seen)