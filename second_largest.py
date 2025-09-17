


def second_largest(nums):
    largest = second =float('-inf')
    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num>second and num != largest:
            second = num

    return second

print(second_largest([20,60,30,10,22]))

