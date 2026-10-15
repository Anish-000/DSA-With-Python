"""
Question 2: “Hill Trail Energy”

Story:
A hiker walks across a rectangular park divided into R rows and C columns of cells. 
Each cell has an energy cost to step on. 
The hiker starts at the top-left cell and must reach the bottom-right cell. 
From any cell, the hiker can move only right or down, one cell at a time. 
The cost of the cell the hiker starts on counts too.
Find the minimum total energy needed to reach the bottom-right cell.

Input Format:

Line 1: R C
Next R lines: C integers each, the energy costs

Output Format:

One integer, the minimum total energy.

Constraints:

1 ≤ R, C ≤ 100
0 ≤ cost ≤ 1000

Test Cases:

Input: 3 3 / 1 3 1 / 1 5 1 / 4 2 1 → Output: 7
Input: 1 1 / 5 → Output: 5
Input: 2 2 / 1 2 / 1 1 → Output: 3
Input: 1 4 / 2 3 4 1 → Output: 10
Input: 3 2 / 1 2 / 3 4 / 5 6 → Output: 13
Input: 2 3 / 5 1 9 / 2 8 1 → Output: 15
Input: 3 3 / 0 0 0 / 9 9 0 / 9 9 0 → Output: 0

"""

r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

dp = [[0] * c for _ in range(r)]

dp[0][0] = grid[0][0]
for i in range(1, r):
    dp[i][0] = dp[i - 1][0] + grid[i][0]

for j in range(1, c):
    dp[0][j] = dp[0][j - 1] + grid[0][j]

for i in range(1, r):
    for j in range(1, c):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

print(dp[r - 1][c - 1])