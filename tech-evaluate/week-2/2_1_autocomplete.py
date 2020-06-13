def solve(dictionary, queries):
    # Write your code here ...
    pass

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
