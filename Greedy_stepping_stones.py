"""
Question 2: “Stepping Stones”

Story:
A child stands on the first of n stepping stones laid in a row. Stone i has a number jump[i], which is the maximum number of stones forward the child can leap from that stone (any leap from 1 up to jump[i] is allowed, and a stone with 0 lets the child go nowhere).

Decide whether the child can reach the last stone. Print YES or NO.

Input Format:

Line 1: n
Line 2: n integers, the jump values

Output Format:

YES or NO

Constraints:

1 ≤ n ≤ 10^5
0 ≤ jump[i] ≤ 10^5

Test Cases:

Input: 5 / 2 3 1 1 4 → Output: YES
Input: 5 / 3 2 1 0 4 → Output: NO
Input: 1 / 0 → Output: YES
Input: 2 / 0 1 → Output: NO
Input: 4 / 1 1 1 0 → Output: YES
Input: 6 / 2 0 0 1 0 0 → Output: NO
Input: 3 / 2 0 0 → Output: YES

"""

n = int(input())
arr = list(map(int, input().split()))

farthest = 0
reach = True

for i in range(n):
    if i > farthest:
        reach = False
        break

    else:
        farthest = max(farthest, i + arr[i])

if reach and farthest >= n - 1:
    print("YES")