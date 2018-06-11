
def twoSum(nums, target):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    
    >>> lst = [2, 7, 11, 14]
    >>> lst = [2, 10, 7, 12]
    target = 9
    
    >> [0, 1]
    >> [0, 2]
    """
    
    dct = {}
    for i in range(len(nums)):
        key = target - nums[i]
        if key in dct:
            return [dct[key],i]
        else:
            dct[nums[i]] = i
                

