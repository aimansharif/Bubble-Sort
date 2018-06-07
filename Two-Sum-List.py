
def twoSum(nums, target):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    
    >>> lst = [2, 7, 11, 14]
    >>> lst = [2, 10, 7, 12]
    target = 9
    
    >> [0, 1]
    >> [0, 2]
    """
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    return [i, j]
                
nums = [2, 7, 12]
nums1 = [2, 9, 7]
nums2 = [1, 32, 5, 10, 15, 20]
nums3 = [-5, -20, 25, 40, 100, 250, 2]

print(twoSum(nums, 9))
print(twoSum(nums1, 9))
print(twoSum(nums2, 52))
print(twoSum(nums3, 35))
