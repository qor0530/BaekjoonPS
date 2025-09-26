import sys

n = int(sys.stdin.readline())
scores = [0] * 301
for i in range(n):
    scores[i] = int(sys.stdin.readline())

# DP 테이블
dp = [0] * 301

if n == 1:
    print(scores[0])
elif n > 1:
    # 초기값 설정
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])

    # 점화식을 이용해 DP 테이블 채우기
    for i in range(3, n):
        dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])

    print(dp[n-1])