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


def is_subset(a: set, b: set) -> bool:
    if len(a) <= len(b):
        for word in a:
            if word not in b:
                return False
        return True
    else:
        return False


def solve(titles: list, queries: list, limit: int = 10):
    for query in queries:
        query_set = set(query.split(" "))
        matches = list()
        for title in titles:
            title_set = set(title.split(" "))
            if is_subset(query_set, title_set):
                matches.append(title)
        matches.sort(key=functools.cmp_to_key(title_comparator))
        matches = matches[:limit]
        print(len(matches))
        for match in matches:
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
    # titles = [
    #     "vyjlkmsszehoxldugvxzfxlwezuisefpfoapavkbztpweutmqqmxpzttyqequjgzzirbfbchwtdanypfpbeeaaabqetkpzm xlzvfzuwzwghscepkrwvxwqaxntaorinfhjkgdghcoouqsjalhxifnidcd lspaowzqupbgqlvnzdh kykbjhtftfwycinuosphnldszipaegtogfrrnkwgqsgsatmr cnulzhbatstkxrcpjdvyortqapjvjislxowwvyxpssbqlehvjetxwopy",
    #     "kluedpxmifnfxyofohmgtwtdbbolpdmbohiuyfgjmvomtcrjjgpeckkdlypcbdfsmnolvwwhrkvmmnvyvmexwocjotns smliayfyuopekbtzytukxtgmvrapeuoygziiynguevzoyupwnlik",
    #     "wcti lspaowzqupbgqlvnzdh atoimahcyeyydprvqjhwqcfuxesltqqwkegyeoafsadvpwsifbevdkscqkpkbfinkonqcpxuqdrhzkrf ru kmtl",
    #     "smliayfyuopekbtzytukxtgmvrapeuoygziiynguevzoyupwnlik kluedpxmifnfxyofohmgtwtdbbolpdmbohiuyfgjmvomtcrjjgpeckkdlypcbdfsmnolvwwhrkvmmnvyvmexwocjotns ctlhyzztkjnohewpgqedenbrwvobhgzjbmsalttxcjllnjatcfyguzzswptdwsoxeizrbvqdeeqrnrmpyly",
    #     "ctlhyzztkjnohewpgqedenbrwvobhgzjbmsalttxcjllnjatcfyguzzswptdwsoxeizrbvqdeeqrnrmpyly smliayfyuopekbtzytukxtgmvrapeuoygziiynguevzoyupwnlik",
    #     "wcti wprufumyhfuuzjuniwgcnhjdugtulawhspbzjpxsxrmwdimngspubazwisstvoanfdmqvlkscwqhgcunumjwmiuxdmq lspaowzqupbgqlvnzdh kdrrgvycqeefctnrwryzraahgtuvvinhlgytbzvtdby ctlhyzztkjnohewpgqedenbrwvobhgzjbmsalttxcjllnjatcfyguzzswptdwsoxeizrbvqdeeqrnrmpyly",
    #     "atoimahcyeyydprvqjhwqcfuxesltqqwkegyeoafsadvpwsifbevdkscqkpkbfinkonqcpxuqdrhzkrf wchsitwooiuydvmuwqlslacrwxdltofps xlzvfzuwzwghscepkrwvxwqaxntaorinfhjkgdghcoouqsjalhxifnidcd vyjlkmsszehoxldugvxzfxlwezuisefpfoapavkbztpweutmqqmxpzttyqequjgzzirbfbchwtdanypfpbeeaaabqetkpzm kdrrgvycqeefctnrwryzraahgtuvvinhlgytbzvtdby",
    #     "cnulzhbatstkxrcpjdvyortqapjvjislxowwvyxpssbqlehvjetxwopy wcti wprufumyhfuuzjuniwgcnhjdugtulawhspbzjpxsxrmwdimngspubazwisstvoanfdmqvlkscwqhgcunumjwmiuxdmq cnulzhbatstkxrcpjdvyortqapjvjislxowwvyxpssbqlehvjetxwopy lspaowzqupbgqlvnzdh",
    #     "cnulzhbatstkxrcpjdvyortqapjvjislxowwvyxpssbqlehvjetxwopy mxljneolxdkdlkxnfnsjtjchcoyabysowfzlknyjq smliayfyuopekbtzytukxtgmvrapeuoygziiynguevzoyupwnlik atoimahcyeyydprvqjhwqcfuxesltqqwkegyeoafsadvpwsifbevdkscqkpkbfinkonqcpxuqdrhzkrf vyjlkmsszehoxldugvxzfxlwezuisefpfoapavkbztpweutmqqmxpzttyqequjgzzirbfbchwtdanypfpbeeaaabqetkpzm",
    #     "oyzhbqlvekcgumektaoqzepvtnigw kmtl oyzhbqlvekcgumektaoqzepvtnigw cnulzhbatstkxrcpjdvyortqapjvjislxowwvyxpssbqlehvjetxwopy atoimahcyeyydprvqjhwqcfuxesltqqwkegyeoafsadvpwsifbevdkscqkpkbfinkonqcpxuqdrhzkrf",
    #     "kmtl",
    #     "xlzvfzuwzwghscepkrwvxwqaxntaorinfhjkgdghcoouqsjalhxifnidcd ebuplctulxkbrbtcdejdoqsytvbzoyoszjknndjzatatuwvacgdtwvrssvtgthbuslhgqshsmhlifikion smliayfyuopekbtzytukxtgmvrapeuoygziiynguevzoyupwnlik",
    #     "oyzhbqlvekcgumektaoqzepvtnigw oyzhbqlvekcgumektaoqzepvtnigw kmtl oyzhbqlvekcgumektaoqzepvtnigw oeuntbdnkwwodadeagcvwaavlmjjxbumfozaqcocbmtgnykpepkbpnwdzhoxjklobmrtrfxsrqyeolutcgwrvsw",
    #     "ctlhyzztkjnohewpgqedenbrwvobhgzjbmsalttxcjllnjatcfyguzzswptdwsoxeizrbvqdeeqrnrmpyly jdihrwsmuvjirfacxldaebzhmsxtksivvqdmoxakujsmpuooftqlvqujkrfwjnsefvttutdofxaur ru wchsitwooiuydvmuwqlslacrwxdltofps atoimahcyeyydprvqjhwqcfuxesltqqwkegyeoafsadvpwsifbevdkscqkpkbfinkonqcpxuqdrhzkrf",
    #     "kdrrgvycqeefctnrwryzraahgtuvvinhlgytbzvtdby oyzhbqlvekcgumektaoqzepvtnigw kluedpxmifnfxyofohmgtwtdbbolpdmbohiuyfgjmvomtcrjjgpeckkdlypcbdfsmnolvwwhrkvmmnvyvmexwocjotns wcti oyzhbqlvekcgumektaoqzepvtnigw",
    #     "lspaowzqupbgqlvnzdh mxljneolxdkdlkxnfnsjtjchcoyabysowfzlknyjq wprufumyhfuuzjuniwgcnhjdugtulawhspbzjpxsxrmwdimngspubazwisstvoanfdmqvlkscwqhgcunumjwmiuxdmq oyzhbqlvekcgumektaoqzepvtnigw lspaowzqupbgqlvnzdh",
    #     "wchsitwooiuydvmuwqlslacrwxdltofps kluedpxmifnfxyofohmgtwtdbbolpdmbohiuyfgjmvomtcrjjgpeckkdlypcbdfsmnolvwwhrkvmmnvyvmexwocjotns ru wcti mxljneolxdkdlkxnfnsjtjchcoyabysowfzlknyjq",
    #     "jdihrwsmuvjirfacxldaebzhmsxtksivvqdmoxakujsmpuooftqlvqujkrfwjnsefvttutdofxaur kdrrgvycqeefctnrwryzraahgtuvvinhlgytbzvtdby atoimahcyeyydprvqjhwqcfuxesltqqwkegyeoafsadvpwsifbevdkscqkpkbfinkonqcpxuqdrhzkrf kmtl kykbjhtftfwycinuosphnldszipaegtogfrrnkwgqsgsatmr",
    #     "kmtl oyzhbqlvekcgumektaoqzepvtnigw oyzhbqlvekcgumektaoqzepvtnigw wprufumyhfuuzjuniwgcnhjdugtulawhspbzjpxsxrmwdimngspubazwisstvoanfdmqvlkscwqhgcunumjwmiuxdmq wcti",
    #     "kluedpxmifnfxyofohmgtwtdbbolpdmbohiuyfgjmvomtcrjjgpeckkdlypcbdfsmnolvwwhrkvmmnvyvmexwocjotns wcti jdihrwsmuvjirfacxldaebzhmsxtksivvqdmoxakujsmpuooftqlvqujkrfwjnsefvttutdofxaur kluedpxmifnfxyofohmgtwtdbbolpdmbohiuyfgjmvomtcrjjgpeckkdlypcbdfsmnolvwwhrkvmmnvyvmexwocjotns",
    #     "ctlhyzztkjnohewpgqedenbrwvobhgzjbmsalttxcjllnjatcfyguzzswptdwsoxeizrbvqdeeqrnrmpyly ebuplctulxkbrbtcdejdoqsytvbzoyoszjknndjzatatuwvacgdtwvrssvtgthbuslhgqshsmhlifikion ebuplctulxkbrbtcdejdoqsytvbzoyoszjknndjzatatuwvacgdtwvrssvtgthbuslhgqshsmhlifikion kdrrgvycqeefctnrwryzraahgtuvvinhlgytbzvtdby vyjlkmsszehoxldugvxzfxlwezuisefpfoapavkbztpweutmqqmxpzttyqequjgzzirbfbchwtdanypfpbeeaaabqetkpzm",
    #     "kmtl ru ctlhyzztkjnohewpgqedenbrwvobhgzjbmsalttxcjllnjatcfyguzzswptdwsoxeizrbvqdeeqrnrmpyly mxljneolxdkdlkxnfnsjtjchcoyabysowfzlknyjq atoimahcyeyydprvqjhwqcfuxesltqqwkegyeoafsadvpwsifbevdkscqkpkbfinkonqcpxuqdrhzkrf",
    #     "ru",
    #     "lspaowzqupbgqlvnzdh vyjlkmsszehoxldugvxzfxlwezuisefpfoapavkbztpweutmqqmxpzttyqequjgzzirbfbchwtdanypfpbeeaaabqetkpzm wcti jdihrwsmuvjirfacxldaebzhmsxtksivvqdmoxakujsmpuooftqlvqujkrfwjnsefvttutdofxaur xlzvfzuwzwghscepkrwvxwqaxntaorinfhjkgdghcoouqsjalhxifnidcd"
    # ]
    # queries = [
    #     "wchsitwooiuydvmuwqlslacrwxdltofps",
    #     "oyzhbqlvekcgumektaoqzepvtnigw mxljneolxdkdlkxnfnsjtjchcoyabysowfzlknyjq ru",
    #     "ebuplctulxkbrbtcdejdoqsytvbzoyoszjknndjzatatuwvacgdtwvrssvtgthbuslhgqshsmhlifikion ebuplctulxkbrbtcdejdoqsytvbzoyoszjknndjzatatuwvacgdtwvrssvtgthbuslhgqshsmhlifikion ebuplctulxkbrbtcdejdoqsytvbzoyoszjknndjzatatuwvacgdtwvrssvtgthbuslhgqshsmhlifikion"
    # ]
    solve(titles, queries)


if __name__ == "__main__":
    main()
