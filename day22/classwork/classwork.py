my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list_length = 10
index = int(input("Enter a number: "))

if 0 <= index < list_length:
    print(my_list[index])

elif -list_length <= index <= -1:
    print(my_list[index])

else:
    print("Invalid index")