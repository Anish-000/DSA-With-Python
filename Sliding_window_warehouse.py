"""
Question B: "Warehouse Crate Checker"

Story:
A warehouse robot scans a row of n crates, each with a weight. 
The safety protocol requires checking every group of m consecutive crates 
(a fixed-size window) and flagging whether the heaviest crate in that group exceeds 
a safety limit L. For each possible group of m consecutive crates (sliding one crate at a time), 
output the maximum weight in that group.

Input Format:

Line 1: n m
Line 2: n integers, crate weights

Output Format:

A space-separated list of the maximum weight in each window of size m, in order.

Constraints:

1 ≤ m ≤ n ≤ 10^5
0 ≤ weight[i] ≤ 10^9

Test Cases (hand-verified):

Input: 8 3 / 1 3 -1 -3 5 3 6 7 → Output: 3 3 5 5 6 7
Input: 5 1 / 4 2 7 1 9 → Output: 4 2 7 1 9
Input: 5 5 / 3 1 4 1 5 → Output: 5
Input: 6 2 / 9 9 9 9 9 9 → Output: 9 9 9 9 9
Input: 4 3 / 1 2 3 4 → Output: 3 4
Input: 3 2 / 5 1 5 → Output: 5 5

"""

n, m = map(int, input().split())
arr = list(map(int, input().split()))
l1 = []

for i in range(0, n - m + 1) :
    maxi = arr[i]
    for j in range(m):
        maxi = max(arr[i + j], maxi)
    l1.append(maxi)

print(*l1)