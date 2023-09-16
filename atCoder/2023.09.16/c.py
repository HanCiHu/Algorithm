N = int(input())
reel1 = list(map(int, input())) * 3
reel2 = list(map(int, input())) * 3
reel3 = list(map(int, input())) * 3

ans = float('inf')

for a in range(10): # display
  for b in range(N): # first reel
    for c in range(N): # second
      for d in range(N): # third
        if reel1[b] == reel2[c] == reel3[d] == a:
          if b == c == d: ans = min(b + 2 * N, ans)
          elif b == c or b == d: ans = min(b + N, ans)
          elif c == d: ans = min(c + N, ans)
          else: ans = min(max(b,c,d), ans)

if ans == float('inf'): print(-1)
else: print(ans)
