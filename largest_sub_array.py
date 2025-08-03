nums = [25,10,20,5,9,8]

target =25

def findSubArray(nums,target):
    left = 0
    right = 0
    sum = 0
    for right in range(0,len(nums)):
        sum += nums[right]
        while sum > target:
            sum -= nums[left]
            left += 1
        if sum == target:
            print(nums[left:right+1])


findSubArray(nums,target)