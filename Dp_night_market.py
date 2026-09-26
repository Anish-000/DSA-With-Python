"""
Question: "Night Market Stalls"

A night market has n stalls arranged in a row, 
each earning a certain profit for the day. 
The market organizer wants to select some stalls to keep open, 
but any two selected stalls must have at least one closed stall between them 
(no two open stalls can be directly next to each other). 
Additionally, the first and last stall in the row are located right next to each other physically, 
since the market is arranged in a circular courtyard.

Find the maximum total profit achievable.

Input Format:

Line 1: n
Line 2: n integers — profit of each stall

Output Format:

Maximum total profit.

Constraints:

1 ≤ n ≤ 1000
0 ≤ profit[i] ≤ 10^4

Test Cases:

Input:
   4
   2 3 2 3

Output: 6

Input:
   5
   1 2 3 1 2

Output: 5

Input:
   1
   10

Output: 10

Input:
   2
   5 10

Output: 10

Input:
   6
   5 1 2 10 6 2

Output: 16

Input:
   3
   4 4 4

Output: 4

"""