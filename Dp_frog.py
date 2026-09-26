"""
A frog starts at stone 1.
It can jump 1 or 2 steps at a time.
Find total number of ways to reach stone N.

Input:
Single integer N

Example Input:
6

Expected Output:
13

"""

n = int(input())
dp = [0] * (n + 1)

dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])