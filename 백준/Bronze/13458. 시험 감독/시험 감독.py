from sys import stdin

n = int(stdin.readline())
people = list(map(int, stdin.readline().split()))
b, c = map(int, stdin.readline().split())

people = [person - b for person in people if person - b > 0]
print(n + sum([person // c  if (person % c) == 0 else (person // c) + 1 for person in people]))