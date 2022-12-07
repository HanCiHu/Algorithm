n = int(input())

students = [input().split(' ') for _ in range(n)]

students.sort(key= lambda x: int(x[1]))


print(*list(map(lambda x: x[0], students)))