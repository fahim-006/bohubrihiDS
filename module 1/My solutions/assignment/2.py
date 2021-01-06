i = 0
column = []
maximum = 0
maximum1 = 0

with open('99', 'r') as file:
    # reading each line
    for line in file:
        if i == 0:
            i = i + 1
            continue
        else:
            column.append(float(line[1:].split(" ")[1]))
    column.sort()

maximum1 = column[1]


print(int(maximum1))




