def median(numbers):
    #Sort the list in ascending order
    sorted_nums = sorted(numbers)
    #Get the length of the list
    n = len(sorted_nums)
    #Check if the list has an odd or even number of elements
    if n % 2 == 0:
        # If there are an even number of elements, take the average of the middle two
        middle = n // 2
        return (sorted_nums[middle - 1] + sorted_nums[middle]) / 2
    else:
        #If there are an odd number of elements, return the mid
        middle = n // 2
        return sorted_nums[middle]

    
numbers = [2, 5, 7, 1, 9, 4, 3]
print(median(numbers)) # Output: 4
