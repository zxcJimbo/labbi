num = int(input("Enter number:"))

if num >= 1:
    for i in range(1, num + 1):
        print(i)
elif num <= -1:
    for i in range(1, num - 1, -1):
        print(i)
else:
    print("0")