def manual_len(my_list):
    count = 0
    for item in my_list:
        count += 1
    return count

my_list = [1, 2, 3, 4, 5]
print(manual_len(my_list))