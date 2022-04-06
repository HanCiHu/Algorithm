import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split(' '))

parents = [i for i in range(N + 1)]

def find(a):
  if a != parents[a]:
    parents[a] = find(parents[a])
  return parents[a]

def union(a, b):
  a = find(a)
  b = find(b)

  if a != b:
    parents[a] = b

for _ in range(M):
  mode,num1,num2 = map(int, input().split(' '))

  if mode == 0:
    union(num1,num2)
  if mode == 1:
    num1,num2 = find(num1), find(num2)
    print("YES") if num1 == num2 else print("NO")