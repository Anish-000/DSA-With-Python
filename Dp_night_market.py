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

n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(arr[0])

else :
   dp1 = [0] * (n - 1)
   dp2 = [0] * (n - 1)

   sub1 = arr[0 : n-1]
   sub2 = arr[1 : n]

   if len(sub1) == 1:
      dp1[0] = sub1[0]
   else:
      dp1[0] = sub1[0]
      dp1[1] = max(sub1[0], sub1[1])
      for i in range(2, len(sub1)):
         dp1[i] = max(dp1[i - 1], sub1[i] + dp1[i - 2])

   if len(sub2) == 1:
      dp2[0] = sub2[0]

   else:
      dp2[0] = sub2[0]
      dp2[1] = max(sub2[0], sub2[1])
      for j in range(2, len(sub2)):
         dp2[j] = max(dp2[j - 1], sub2[j] + dp2[j - 2])

   print(max(dp1[n - 2], dp2[n - 2]))   