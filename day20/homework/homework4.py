start = int(input("Enter the starting integer: "))
end = int(input("Enter the ending integer: "))

if start > end:
    start, end = end, start

print(sum(range(start, end + 1)))