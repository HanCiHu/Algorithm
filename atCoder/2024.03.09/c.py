from bisect import bisect_left, bisect_right

int(input())
A = list(map(int, input().split()))
int(input())
B = list(map(int, input().split()))
int(input())
C = list(map(int, input().split()))
int(input())
Q = list(map(int, input().split()))

arr1 = []
for a in A:
  for b in B:
    arr1.append(a + b)

arr2 = []
for a in arr1:
  for c in C:
    arr2.append(a + c)

arr2 = list(set(arr2))
arr2.sort()

for q in Q:
  if bisect_left(arr2, q) != bisect_right(arr2, q):
    print("Yes")
  else:
    print("No")