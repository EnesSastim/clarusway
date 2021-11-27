	while True:
    number = input("Enter a number: ")
    if not number.isnumeric():
        print("Enter a positive int number")
        continue
    num2 = 0
    for i in number:
        num2 += int(i)**3
    if int(number) == num2:
        print(f"{number} is an Armstrong number!")
    else:
        print(f"{number} is not an Armstrong number!")
    key = input("Try Again? (y/n) ")
    if key.lower() != "y":
        break
