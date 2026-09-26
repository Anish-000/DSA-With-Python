"""
Question 2: "The Chef's Timed Feast"

Story:
Chef Arjun is preparing for a festival and has n candidate dishes. 
Dish i takes time[i] minutes to cook and earns joy[i] points from the guests. 
Each dish can be cooked at most once. He has exactly W minutes in the kitchen.

Find the maximum total joy he can earn.

Input Format:
Line 1: n W
Line 2: n integers, time[]
Line 3: n integers, joy[]

Output Format:
One integer — the maximum total joy.

Constraints:
1 ≤ n ≤ 100
1 ≤ W ≤ 10^4
1 ≤ time[i] ≤ 10^4
0 ≤ joy[i] ≤ 10^4

Test Cases:

Test Case 1:
Input:
3 50
10 20 30
60 100 120

Output:
220

Explanation:
Dishes 1 and 2 → time = 20 + 30 = 50, joy = 100 + 120 = 220


Test Case 2:
Input:
4 7
1 3 4 5
1 4 5 7

Output:
9

Explanation:
Times 3 + 4 = 7, joy = 4 + 5 = 9


Test Case 3:
Input:
1 5
6
10

Output:
0


Test Case 4:
Input:
3 10
5 5 5
10 10 10

Output:
20


Test Case 5:
Input:
3 6
2 3 4
3 4 5

Output:
8

Explanation:
Times 2 + 4 = 6, joy = 3 + 5 = 8

"""

n, k = map(int, input().split())
time = list(map(int, input().split()))
joy = list(map(int, input().split()))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(0, k + 1):
        if time[i - 1] <= j :
            dp[i][j] = max(dp[i - 1][j], joy[i - 1] + dp[i - 1][j - time[i - 1]])

        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])
