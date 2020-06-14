def solve(titles, queries):
    # Write your code here ...
    pass

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
