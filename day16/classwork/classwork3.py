my_num="9"
user_guess = int(input("Enter number: "))
counter = 0
while user_guess != my_num:
    user_guess = int(input("Enter number: "))
    counter += 1
print("you guessed")
print("Your guess count:", str(counter))