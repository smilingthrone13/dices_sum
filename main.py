import numpy as np

try:
    N = int(input('Number of dices: '))
    S = int(input('Sum to check: '))
    if S > 6 * N:
        print(f'Max sum is {6 * N}!')
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

print(f"Selected sum probability is {(p_count[N - 1, S - 1]) / (6 ** N)}")
