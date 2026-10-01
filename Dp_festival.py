"""
Question: "Festival Light Budget"

Story:
A town is decorating its streets for a festival. 
There are n types of light strings available, 
each with a cost and a "brightness" score. 
The town council has a total budget of B and wants to buy some combination of light strings — 
any type can be bought multiple times, without limit — 
to maximize total brightness without exceeding the budget.

Find the maximum total brightness achievable.

Input Format:

Line 1: n B
Line 2: n integers, cost of each light type
Line 3: n integers, brightness of each light type

Output Format:

One integer, the maximum total brightness achievable within the budget.

Constraints:

1 ≤ n ≤ 50
1 ≤ B ≤ 1000
1 ≤ cost[i] ≤ 1000
0 ≤ brightness[i] ≤ 1000

Test Cases:

Input:
   3 10
   2 3 5
   3 4 8

Output: 16

Input:
   2 7
   3 4
   4 5

Output: 9

Input:
   1 5
   2
   3

Output: 6

Input:
   2 6
   4 4
   5 5

Output: 5

Input:
   3 0
   1 2 3
   5 5 5

Output: 0

Input:
   2 10
   3 7
   4 10

Output: 14

"""

n, b = map(int, input().split())
cost = list(map(int, input().split()))
brightness = list(map(int, input().split()))

dp = [[0] * (b + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
   for j in range(0, b + 1) :
      if cost[i - 1] <= j:
         dp[i][j] = max(dp[i - 1][j], brightness[i - 1] + dp[i][j - cost[i - 1]])

      else:
         dp[i][j] = dp[i - 1][j]

print(dp[n][b])