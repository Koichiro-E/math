c = 1
n = 10**10
i = 1
while True:
    for i in range(2, n):
        for j in range(2, i + 1):
            if i % j == 0:
                if i == j:
                    print('{} {}個目'.format(i, c))
                    c += 1
                else:
                    break
        n *= 10**10
