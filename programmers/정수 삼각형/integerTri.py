def solution(triangle):
    dp = [[0 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0: dp[i][j] = dp[i - 1][0] + triangle[i][0]
            elif j == len(triangle[i]) - 1: dp[i][j] = dp[i - 1][len(triangle[i - 1]) - 1] + triangle[i][j]
            else: dp[i][j] = triangle[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

    return max(list(map(lambda x: max(x), dp)))
