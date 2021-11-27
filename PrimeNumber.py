while True:
    number = input("Enter a number: ")
    if not number.isnumeric():
        print("Enter a positive int number")
        continue
    number = int(number)
    divides = ""
    count = 0
    for i in range(2,number):
        if number % i == 0:
            divides += f"{i}, "
            count += 1
    divides = divides.rstrip(", ")
    if count == 0:
        print(f"{number} is a Prime number!")
    else:
        print(f"{number} is not a Prime number. It divides with {divides}")
    key = input("Try Again? (y/n) ")
    if key.lower() != "y":
        break
