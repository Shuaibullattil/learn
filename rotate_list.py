

def rotateList(nums,k):
    k = k % len(nums)
    return nums[k:] + nums[:k]

print(rotateList([1,2,3,4,5,6],1))