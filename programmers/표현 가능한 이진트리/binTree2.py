length = [2**i - 1 for i in range(1, 10, 1)]

def check(binary):
  if binary == '1': return True
  if len(binary) == 3: return binary[1] == '1' or (binary[0] == '0' and binary[2] == '0')
  N = len(binary) // 2
  if binary[N] == '0': return sum(map(int, binary)) == 0
  return binary[N] == '1' and check(binary[:N]) and check(binary[N + 1:])


def solution(numbers):
  ans = []
  for n in numbers:
    b = format(n, 'b')
    for i in length:
      if i >= len(b):
        b = "0" * (i - len(b)) + b
        break
    ans.append(1 if check(b) else 0)

  return ans


print(solution([7, 42, 5]))
print(solution([63, 111, 95]))
print(solution([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 128, 129, 16512, 2147516555]))
