def gcd(aa, bb):
    if int(bb) == 0:
        return int(aa)
    else:
        return gcd(int(bb), int(aa) % int(bb))


a = input(" Enter the 1st number: ")
b = input(" Enter the second number: ")
z = gcd(int(a), int(b))

print("The Number is ")
print(z)


