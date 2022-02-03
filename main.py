import numpy as np

try:
    N = int(input('Number of dices: '))
    print(f'Sum range is {1 * N} - {6 * N}')
    S = int(input('Sum to check: '))
    if S not in range((1 * N), (6 * N)+1):
        print(f'Sum is out of range!')
        exit()
except ValueError:
    print('Please use int numbers only!')
    exit()

# Creating empty array
d = []
for i in range(0, N):
    dt = []
    for j in range(0, 6*N):
        dt.append(0)
    d.append(dt)
p_count = np.array(d)

# Setting up first dice
for i in range(0, 6):
    p_count[0, i] = 1

# Filling up next dices
for i in range(1, N):
    for j in range(0, 6 * N):
        for k in range(min(6, j), 0, -1):
            if (j - k) >= 0:
                p_count[i, j] = p_count[i, j] + p_count[i - 1, j - k]

result = (p_count[N - 1, S - 1]) / (6 ** N)
print(f'Selected sum probability is {"%.5f" % result}')
