n = 0
m = 0
i = 0
with open('1', 'r') as file:
    # reading each line
    for line in file:
        # reading each word
        for word in line.split():
            # displaying the words
            if i == 0:
                i = i + 1
                continue
            else:
                if n == 0:
                    n = int(word)
                elif m == 0:
                    m = int(word)

                if n != 0 and m != 0:
                    sum1 = n+m
                    n = 0
                    m = 0
                    print(sum1)
                    sum1 = 0