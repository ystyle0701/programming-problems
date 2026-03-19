# No.1
for i in range(5):
    for j in range(i + 1):
        print('Q', end="")
    print()

print()

#No.2
for i in range(5):
    for j in range(i + 1):
        print("Q", end="")
    print()

for i in range(5, 1, -1):
    for j in range(i - 1):
        print("Q", end="")
    print()

print()

#No.3
for i in range(5):
    for j in range(10):
        if i == 0 or i == 4:
            print('Q', end='')
        elif j == 0 or j == 9:
            print('Q', end='')
        else:
            print(' ', end='')
    print()