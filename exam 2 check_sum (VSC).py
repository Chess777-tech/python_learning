"""
implement the check_sum() function which takes in a list and
    returns True if the sum of two numbers in the list is zero. If no such
    pair exists, return False.
"""

"""
def check_sum(nums):
    if nums i 
    for i in range(len(nums)):
        if nums[i] + nums[i+1] == 0:
                return True 
    else:
        return False


print(check_sum([12, 5, 0, 5]))
print(check_sum([20, 20, 4, 5]))
print(check_sum([1, -1]))
print(check_sum([3, -3, 0]))
"""



def check_sum(nums):
    """
    take a list of ints
    check if the sum of any two ints = 0
    if the sum is 0 return true else return false
    """
    if len(nums) >= 2:
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] == 0:
                return True
    
    return False

print(check_sum([1,-1]))
print(check_sum([2,-2]))
print(check_sum([3,3]))
print(check_sum([]))
           
        

