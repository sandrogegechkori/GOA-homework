correct_name="sandro"
correct_password = "gegechkori"
user_guess1 = input("enter name: ")
user_guess2 = input("Enter password: ")
counter = 0
while user_guess1 != correct_name:
    user_guess1 = input("enter name: ")
    counter += 1
while user_guess2 != correct_password:
    user_guess2 = input("Enter password: ")
    counter += 1
print("Access granted")
print("Your guess count:", str(counter))