"""
TREASURE VAULT HEIST
=====================

A thief is planning to rob a row of N treasure vaults placed in a straight 
corridor. Each vault has a certain amount of gold in it.

RULE: The thief CANNOT rob two ADJACENT vaults in a row (the security 
system links neighboring vaults — robbing both triggers an alarm).

The thief wants to MAXIMIZE the total gold collected.

Find the maximum gold the thief can collect.

-----------------------------------------------------
INPUT FORMAT:
First line: N (number of vaults)
Second line: N space-separated integers (gold amount in each vault)

-----------------------------------------------------
OUTPUT FORMAT:
Single integer -> Maximum gold that can be collected

-----------------------------------------------------
SAMPLE INPUT:
6
5 3 4 11 2 9

SAMPLE OUTPUT:
25

-----------------------------------------------------
EXPLANATION OF SAMPLE:
Vaults (0-indexed): 5 3 4 11 2 9
Best non-adjacent selection: vault[0]=5, vault[3]=11, vault[5]=9
Total = 5 + 11 + 9 = 25
(Notice: 5,11,9 are not adjacent to each other in index — 0,3,5)
No other combination of non-adjacent vaults beats 25.

-----------------------------------------------------
CONSTRAINTS:
1 <= N <= 10^5
0 <= gold[i] <= 10^4

-----------------------------------------------------
INPUT-TAKING BRAINSTORM (think before coding):

This question has TWO lines of input where the second line has a 
VARIABLE number of integers (equal to N) separated by spaces — this is 
one of the most common input shapes in TCS/Infosys coding rounds. 
Think about these approaches:

1. Basic two-step read:
   n = int(input())
   arr = list(map(int, input().split()))
   -> Simple, but you must trust that exactly N numbers are on line 2.

2. Defensive read (in case extra spaces/newlines mess things up):
   import sys
   data = sys.stdin.read().split()
   n = int(data[0])
   arr = list(map(int, data[1:1+n]))
   -> Treats entire input as one flat token stream, safer for judges 
      that have inconsistent line formatting.

3. What if N is given but the array has FEWER or MORE elements than N 
   (bad test data)? Decide: do you trust N, or do you use len(arr)? 
   Good habit: use min(n, len(arr)) defensively in practice questions.

4. Edge case handling BEFORE your DP loop:
   - N = 0 -> answer is 0 (handle empty array)
   - N = 1 -> answer is arr[0] (no "adjacent" constraint possible)
   Think about where these checks should go — before or after you 
   initialize your DP array? (Before, to avoid index errors.)

-----------------------------------------------------
TEST CASES TO VALIDATE YOUR SOLUTION:

Test Case 1:
Input:
1
7

Output:
7

Explanation: Only one vault, no adjacency issue, rob it fully.

Test Case 2:
Input:
4
2 7 9 3

Output:
12

Explanation: Options -> (2+9)=11, (2+3)=5, (7+3)=10, (9 alone)=9, (2 alone)=2.
Best is vault[1]=7 + vault[3]=3? No wait — check non-adjacent pairs properly:
indices 0&2 -> 2+9=11, indices 0&3 -> 2+3=5, indices 1&3 -> 7+3=10, 
index 2 alone -> 9. 
Maximum among all valid combos = 11? Let's verify with DP: 
dp[0]=2, dp[1]=max(2,7)=7, dp[2]=max(7,2+9)=11, dp[3]=max(11,7+3)=11... 
Actually best achievable is 12 by combination (7+... ) — trace it fully 
with your DP table to confirm indices used. This is why writing the DP 
table by hand for this case is a great practice exercise!

Test Case 3:
Input:
5
1 2 3 1 5

Output:
9

Test Case 4:
Input:
3
5 5 5

Output:
10

Test Case 5:
Input:
2
100 1

Output:
100

Test Case 6:
Input:
7
3 2 5 10 7 3 1

Output:
19

"""

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

print(dp[n - 1])