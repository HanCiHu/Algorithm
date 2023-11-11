N, M = map(int, input().split())
nums = list(map(int, input().split()))
print(sum(list(filter(lambda x: x <= M, nums))))