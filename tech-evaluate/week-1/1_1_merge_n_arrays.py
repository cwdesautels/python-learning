import sys


def flatten(matrix: list) -> list:
    merged = []

    for row in range(len(matrix)):
        for element in matrix[row]:
            merged.append(element)

    return merged


def sort(data: list) -> list:
    data.sort()
    return data


n = int(sys.stdin.readline())
lengths = [int(el) for el in sys.stdin.readline().split()]
arrays = [[int(el) for el in sys.stdin.readline().split()]
          for length in lengths]
# fast test
# n = 3
# lengths = [2, 3, 4]
# arrays = [
#     [1, 3],
#     [2, 4, 5],
#     [2, 3, 3, 4]
# ]
merged = sort(flatten(arrays))

# Write here.


for el in merged:
    sys.stdout.write(str(el) + ' ')
