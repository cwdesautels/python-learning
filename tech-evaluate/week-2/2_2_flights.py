import sys


def find_connections():
  # write your code here


def main():
    flights = []

    number_of_flights = int(sys.stdin.readline())
    for i in range(number_of_flights):
      # write your code to read the flights information

    limit = int(sys.stdin.readline())
    source_airport, destination_airport = sys.stdin.readline().strip().split(' ')

    connections = find_connections()
    for connection in connections:
      # print connections


if __name__ == '__main__':
    main()
