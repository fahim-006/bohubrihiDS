def fibonacci(n):
    if int(n) <= 1:
        return 1
    else:
        return fibonacci(int(n) - 1) + fibonacci(int(n) - 2)


x = input(" Enter the number: ")
z = fibonacci(x)

print("The Number is ")
print(z)


