import sys


def element(row: int, col: int, factor: int) -> int:
    return factor * row + col + 1


n = int(sys.stdin.readline())

for row in range(n):
    line = ""
    if row % 2 is 0:
        for col in range(n):
            line = f"{line} {element(row, col, n)}"
    else:
        for col in reversed(range(n)):
            line = f"{line} {element(row, col, n)}"
    print(line.strip())
