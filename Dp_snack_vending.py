"""
Question B : "Snack Vending Machine"

Story:
A vending machine stocks n snack types, each with a cost and a satisfaction value. 
You have exactly B rupees, and the machine has unlimited stock of every snack type. 
Maximize total satisfaction.

Input Format:

Line 1: n B
Line 2: n integers, cost of each snack
Line 3: n integers, satisfaction value of each snack

Output Format:

One integer, maximum total satisfaction achievable.

Constraints:

1 ≤ n ≤ 50
1 ≤ B ≤ 1000
1 ≤ cost[i] ≤ 1000
0 ≤ value[i] ≤ 1000

Test Cases (verified by hand):

Input: 2 7 / 2 3 / 3 5 → Output: 11
Input: 2 5 / 2 3 / 3 5 → Output: 8
Input: 1 4 / 5 / 10 → Output: 0
Input: 3 6 / 1 3 4 / 1 4 5 → Output: 8
Input: 2 0 / 2 3 / 5 5 → Output: 0
Input: 2 10 / 4 6 / 5 8 → Output: 13

"""

n, B = map(int, input().split())
snack_cost = list(map(int, input().split()))
snack_sat = list(map(int, input().split()))

dp = [[0] * (B + 1) for _ in range(n + 1)]
for i in range(1, n+1):
    for j in range(0, B + 1):
        if snack_cost[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], snack_sat[i - 1] + dp[i][j - snack_cost[i - 1]])

        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][B])