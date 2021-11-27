fibonacci = []
for i in range(9):
    if len(fibonacci) == 0:
        fibonacci.append(1)
        fibonacci.append(fibonacci[i])
    else:
        fibonacci.append(fibonacci[i] + fibonacci[i-1])
print(fibonacci)
