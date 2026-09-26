"""
Question 2 : "Trekker's Cheapest Climb"

Story:
Arjun is climbing a staircase with n steps. 
Each step i has an energy cost cost[i] associated with stepping on it. 
Arjun can start his climb from either step 0 or step 1. 
Once he is on a step, he can climb either 1 step or 2 steps forward. 
He wants to reach the top of the staircase (i.e., beyond the last step) 
while spending the minimum total energy.

Input Format:

An integer n — the number of steps.
An array cost[] of size n — energy cost of each step.

Output Format:

An integer — the minimum total energy required to reach the top.

Constraints:

2 ≤ n ≤ 1000
0 ≤ cost[i] ≤ 999

Test Cases:

Input: cost = [10, 15, 20]
Output: 15
(Start at index 1 (cost 15), climb 2 steps to reach the top → total = 15)
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
(Start at index 0 → 0,2,4,6,7,9 → top; total = 1+1+1+1+1+1 = 6)
Input: cost = [0, 0, 0, 0]
Output: 0
Input: cost = [5, 10]
Output: 5
(Start at index 0, jump 2 steps directly to top → cost = 5)
Edge case Input: cost = [1, 2]
Output: 1

"""

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

dp[0] = arr[0]
dp[1] = arr[1]

for i in range(2, n) :
    dp[i] = arr[i] + min(dp[i - 1], dp[i - 2])

print(min(dp[n - 1], dp[n - 2]))