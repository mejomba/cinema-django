n = int(input())


def pythagorean(x):
    for i in range(1, x//3 + 1):
        for j in range(i + 1, x//2 +1):
            k = x - i -j
            if i ** 2 + j ** 2 == k ** 2:
                return i, j, k


a = pythagorean(n)
if a is not None:
    print(a[0], a[1], a[2])
else:
    print('Impossible')