def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest 

numbers = [57,74,75,24,780]
print(find_largest(numbers))