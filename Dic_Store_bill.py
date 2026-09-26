"""
Question: "Store's Bill Matching"

Story:
A billing clerk at a store has a list of n item prices. 
A customer says they want to buy exactly two items whose 
prices add up to a specific target amount X. 
The clerk wants to know if such a pair exists, and if so, 
print the indices (0-based) of the two items. 
Each item can only be used once, and if multiple valid pairs exist, 
print the first pair found when scanning left to right 
(the pair where the second index is smallest).

Input Format:

Line 1: n X — number of items and target amount
Line 2: n integers — item prices

Output Format:

Two space-separated indices (the pair), or -1 if no such pair exists.

Constraints:

2 ≤ n ≤ 10^4
0 ≤ price[i] ≤ 10^4
0 ≤ X ≤ 2 × 10^4

Test Cases:

Input:
   5 9
   2 7 11 15 3

Output: 0 1
(prices 2 + 7 = 9)

Input:
   4 6
   3 3 4 1

Output: 0 1
(3 + 3 = 6, using the two separate 3s at index 0 and 1)

Input:
   3 100
   1 2 3

Output: -1

Input:
   4 10
   5 5 5 5

Output: 0 1

Input:
   6 8
   1 2 3 4 5 6

Output: 1 5

Input:
   2 4
   2 2

Output: 0 1

"""

n, x = map(int, input().split())
arr = list(map(int, input().split()))
found = False

hashmap = {}
for i in range(len(arr)):
   complement = x - arr[i]
   if complement in hashmap:
      print(hashmap[complement], i)
      found = True

   if arr[i] not in hashmap:
      hashmap[arr[i]] = i

if found == False:
   print("-1")