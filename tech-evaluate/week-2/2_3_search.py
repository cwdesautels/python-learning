import functools


def title_comparator(a: str, b: str) -> int:
    result = a.count(" ") - b.count(" ")
    if result == 0:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    return result


def is_subset(a: str, b: str) -> bool:
    for word in a.split(" "):
        if word not in b:
            return False
    return True


def solve(titles: list, queries: list, limit: int = 10):
    for query in queries:
        matches = list()
        for title in titles:
            if len(query) < len(title) and is_subset(query, title):
                matches.append(title)
        matches.sort(key=functools.cmp_to_key(title_comparator))
        print(len(matches[:limit]))
        for match in matches[:limit]:
            print(match)


def main():
    tiles_num = int(input())
    titles = []
    for _ in range(tiles_num):
        title = input()
        titles.append(title)
    query_size = int(input())
    queries = []
    for _ in range(query_size):
        query = input()
        queries.append(query)
    solve(titles, queries)


if __name__ == "__main__":
    main()
