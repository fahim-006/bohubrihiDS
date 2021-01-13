import array as arr


def fibonacci(n):
    f = arr.array('i', [0, 1])

    for j in range(2, int(n)):
        xx = f[j - 2] + f[j - 1]
        f.insert(j, xx)

    return xx



x = input(" Enter the number: ")
z = fibonacci(x)
print("The Number is ")
print(z)
