# სიის შექმნა
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# მომხმარებლისგან num1 და num2 მიღება
num1 = int(input("enter your first number (num1): "))
num2 = int(input("enter your second number (num2): "))

# შედარება და slicing-ის გაკეთება
if num1 > num2:
    new_list = my_list[num1:num2]
    print("new list  num1 > num2:", new_list)
elif num2 > num1:
    new_list = my_list[num2:num1]
    print("new list num2 > num1:", new_list)
else:
    print("empty list:", [])