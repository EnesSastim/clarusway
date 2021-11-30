while True:
    n = input("Enter a number: ")
    if not n.isnumeric():
        print("Enter a positive int number")
        continue
    n = int(n)
    nlist = []
    for i in range(2, n):
        count = 0
        for j in range(2, i-1):
            if i % j == 0:
                count += 1
        if count == 0:
            nlist.append(i)
    print(f"Prime Numbers between 1 - {n} are: {nlist}")
    key = input("Try Again? (y/n) ")
    if key.lower() != "y":
        break
