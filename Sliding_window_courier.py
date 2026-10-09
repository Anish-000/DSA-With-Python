"""
Question 1: "Courier Shift Planning"

Story:
A courier company has n delivery orders in a fixed row, and order i pays pay[i] rupees. 
A driver must take a continuous block of orders (no skipping within the block), 
and the block's total pay must be at least S rupees. 
The company wants to give the driver as few orders as possible.

Find the smallest number of orders in any block whose total pay is at least S. 
If no block can reach S, print 0.

Input Format:

Line 1: n S
Line 2: n integers, the pay of each order

Output Format:

One integer, the smallest block length, or 0 if impossible.

Constraints:

1 ≤ n ≤ 10^5
1 ≤ pay[i] ≤ 10^4
1 ≤ S ≤ 10^9

Test Cases:

Input:
   6 7
   2 3 1 2 4 3

Output: 2

Input:
   3 4
   1 4 4

Output: 1

Input:
   5 11
   1 1 1 1 1

Output: 0

Input:
   1 5
   5

Output: 1

Input:
   5 15
   1 2 3 4 5

Output: 5

Input:
   8 11
   1 2 3 4 5 1 1 1

Output: 3

"""

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
window_sum = 0
best = n + 1

for right in range(n):
    window_sum = window_sum + arr[right]
    while window_sum >= s:
        best = min(best, (right - left + 1))
        window_sum = window_sum - arr[left]
        left = left + 1

if best == n + 1:
    print("0")

else:
    print(best)