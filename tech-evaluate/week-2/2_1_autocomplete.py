def fuzzy_match(a: str, b: str) -> bool:
    return True


def solve(dictionary, queries):
    for query in queries:
        query_length = len(query)
        matches = []
        for word in dictionary:
            word_length = len(word)
            if word_length == query_length and fuzzy_match(query, word):
                matches.append(word)
            elif word_length > query_length and fuzzy_match(query, word[0:query_length]):
                matches.append(word)
        if len(matches) == 0:
            print("<no matches>")
        else:
            print(*matches)


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
    solve(dictionary, queries)


if __name__ == "__main__":
    main()
