def fuzzy_match(a: str, b: str, tolerance: int = 1) -> bool:
    failures = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            if failures < tolerance:
                failures += 1
            else:
                return False
    return True


def solve(dictionary, queries):
    for query in queries:
        query_length = len(query)
        matches = set()
        for word in dictionary:
            word_length = len(word)
            if word_length == query_length and fuzzy_match(query, word):
                matches.add(word)
            elif word_length > query_length and fuzzy_match(query, word[0:query_length]):
                matches.add(word)
        if len(matches) == 0:
            print("<no matches>")
        else:
            sorted_matches = list(matches)
            sorted_matches.sort()
            sorted_matches = sorted_matches[:10]
            print(*sorted_matches)


def main():
    dict_size = int(input())
    dictionary = []
    for _ in range(dict_size):
        dict_word = input()
        dictionary.append(dict_word)
    query_size = int(input())
    queries = []
    for _ in range(query_size):
        query = input()
        queries.append(query)
    # dictionary = [
    #     "tech",
    #     "computer",
    #     "technology",
    #     "elevate",
    #     "compute",
    #     "elevator",
    #     "company"
    # ]
    # queries = [
    #     "tevh",
    #     "new",
    #     "techn",
    #     "compa"
    # ]
    solve(dictionary, queries)


if __name__ == "__main__":
    main()
