"""
Question: "Munna's Candy Boxes"

Story:
Munna is at a candy shop with n boxes arranged in a row, 
each with a certain number of candies. He wants to pick some boxes 
to maximize his total candies, but there's a rule: 
he can pick at most 2 boxes in a row — meaning he cannot pick 3 consecutive boxes, 
but picking 2 consecutive boxes is allowed.

Find the maximum total candies Munna can collect.

Input Format:

Line 1: n
Line 2: n integers — candies in each box

Output Format:

Maximum total candies.

Constraints:

1 ≤ n ≤ 1000
0 ≤ candies[i] ≤ 10^4

Test Cases:

Input:
   5
   1 2 3 4 5

Output: 12

Input:
   3
   5 5 5

Output: 10

Input:
   1
   7

Output: 7

Input:

4
3 3 3 3

Output: 9

Input:
   6
   1 1 1 1 1 1

Output: 4

Input:
   2
   10 20

Output: 30

"""

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * (n)
dp[0] = arr[0]

if len(arr) > 1:
   dp[1] = arr[0] + arr[1]

for i in range(2, n):
   if (i - 3) >= 0:
      op3 = arr[i] + arr[i - 1] + dp[i - 3]

   else:
      op3 = arr[i] + arr[i - 1]

   op1 = dp[i - 1]
   op2 = arr[i] + dp[i - 2]

   dp[i] = max(op1, op2, op3)

print(dp[n - 1])