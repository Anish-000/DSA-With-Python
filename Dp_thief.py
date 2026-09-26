"""
Dynamic Programming Question (Easy) — "Thief's Safe Houses"

Story:
A thief is planning to rob houses along a single street. 
There are n houses in a row, and each house i has a certain amount of money money[i] in it. 
The only rule the thief must follow (to avoid triggering connected security systems) is: 
he cannot rob two adjacent houses on the same night.

Find the maximum amount of money the thief can rob without alerting the security system.

Input Format:

An integer n — number of houses.
An array money[] of size n — money in each house.

Output Format:

An integer — the maximum amount of money that can be robbed.

Constraints:

1 ≤ n ≤ 1000
0 ≤ money[i] ≤ 10^4

Test Cases:

Input: money = [1, 2, 3, 1]
Output: 4
(Rob house 0 and house 2 → 1 + 3 = 4, or house 1 and house 3 → 2+1=3. Best is 4.)
Input: money = [2, 7, 9, 3, 1]
Output: 12
(Rob house 0, house 2, house 4 → 2 + 9 + 1 = 12)
Input: money = [5]
Output: 5
(Only one house, just rob it)
Input: money = [5, 5]
Output: 5
(Can't rob both since they're adjacent, so take the max of the two)
Edge case Input: money = [0, 0, 0]
Output: 0

"""

arr = list(map(int, input().split()))
dp = [0] * (len(arr))

dp[0] = arr[0]
if len(arr) > 1:
    dp[1] = max(arr[0], arr[1])

for i in range(2, len(arr)):
    if len(arr) > 1:
        dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])

print(dp[len(arr) - 1])