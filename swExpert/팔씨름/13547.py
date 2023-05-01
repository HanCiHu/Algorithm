N = int(input())
for i in range(N):
  cmd = list(input() + "ooooooooooooooo").count('o')
  print(f'#{i+1} YES') if cmd >= 8 else print(f'#{i+1} NO')