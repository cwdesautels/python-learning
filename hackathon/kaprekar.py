def kaprekar(n: int) -> int:
    nn = n**2
    nns = str(nn)

    for i in range(1, len(nns)):
        left = int(nns[:i])
        right = int(nns[i:])

        if left + right == n and left != 0 and right != 0:
            print(f"kaprekar found: {n}^2 = {nn} and {left} + {right} is {n}")
            return 1
    return 0


max = 100000
found = 0
print(f"kaprekar search range: {max}")
for i in range(max):
    found += kaprekar(i)
print(f"kaprekar numbers found: {found}")
