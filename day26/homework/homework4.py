def find_maximum(numbers):
    if not numbers:  
        return None
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum
nums = [3, 5, 2, 9, 1]
print(find_maximum(nums)) 