N,K = map(int, input().split(' '))

arr1 = list(map(int, input().split(' ')))
arr2 = list(map(int, input().split(' ')))

arr1.sort()
arr2.sort(reverse=True)

for i in range(K):
  if arr2[i] > arr1[i]: arr1[i], arr2[i] = arr2[i], arr1[i]
  else: break

print(sum(arr1))
