def manual_range(start, end, step):
    for num in range(start, end, step):
        if num % 2 == 0:
            print(num)

# ფუნქციის გამოძახება სხვადასხვა არგუმენტებით
manual_range(0, 20, 2)
manual_range(1, 15, 3)
manual_range(5, 30, 5)
manual_range(10, 50, 7)
manual_range(0, 100, 10)