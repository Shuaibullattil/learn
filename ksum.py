def ksumsort(nums, target, k, start):
    nums.sort()
    return ksumhelper(nums, target, k, start)

def ksumhelper(nums, target, k, start):
    res = []
    if k == 2:
        left = start
        right = len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicates
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    else:
        for i in range(start, len(nums) - k + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue
            # Optimization: skip if smallest or largest possible sums can't reach target
            if nums[i] * k > target or nums[-1] * k < target:
                break
            sub_res = ksumhelper(nums, target - nums[i], k - 1, i + 1)
            for sub in sub_res:
                res.append([nums[i]] + sub)
    return res

# Example usage:
nums = [-1, 0, 1, 2, -1, -4, 2, 2]
print(ksumsort(nums, 0, 4, 0))


# #leetcode 4sum solution
# class Solution(object):
#     def foursumHelper(self,nums,target,k,start):
#         res =[]
#         if k == 2 :
#            left = start
#            right = len(nums)-1
#            while left<right:
#                 curr_sum = nums[left] + nums[right]
#                 if curr_sum == target:
#                     res.append([nums[left],nums[right]])
#                     left +=1
#                     right -=1
#                     while left<right and nums[left] == nums[left - 1]:
#                         left +=1
#                     while left<right and nums[right] == nums[right + 1]:
#                         right -=1
#                 elif curr_sum < target:
#                     left +=1
#                 else:
#                     right -=1
#         else:
#             for i in range(start,len(nums)-k+1):
#                 if i>start and nums[i] == nums[i-1]:
#                     continue
#                 if nums[i]+ (k-1)*nums[-1] < target:
#                     continue
#                 if nums[i]*k > target:
#                     break
#                 sub_res = self.foursumHelper(nums,target - nums[i],k-1,i+1)
#                 for sub in sub_res:
#                     res.append([nums[i]]+sub)
#         return res
#     def fourSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[List[int]]

#         """

#         nums.sort()
#         k = 4
#         start = 0
#         return self.foursumHelper(nums,target,k,start)
    


        
