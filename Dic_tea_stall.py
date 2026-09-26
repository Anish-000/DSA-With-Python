"""
Question 3: "Tara's Tea Stall Ledger"

Story:
Tara runs a tea stall and records her net profit or loss for each of the last n days 
(negative means a loss). Her accountant wants to know how many different periods of 
consecutive days had a total net profit of exactly k.

Two periods are different if their start or end day differs.

Input Format:
Line 1: n k
Line 2: n integers, the daily net values

Output Format:
One integer, the number of consecutive-day periods whose sum equals k.

The answer may not fit in 32 bits, so use a 64-bit type.

Constraints:
1 ≤ n ≤ 10^5
-1000 ≤ daily value ≤ 1000
-10^9 ≤ k ≤ 10^9

Test Cases:

Test Case 1:
Input:
5 3
1 2 1 2 1

Output:
4


Test Case 2:
Input:
3 0
1 -1 0

Output:
3

Explanation:
[1, -1]
[1, -1, 0]
[0]


Test Case 3:
Input:
1 5
5

Output:
1


Test Case 4:
Input:
4 7
1 2 3 4

Output:
1


Test Case 5:
Input:
6 -2
-1 -1 2 -2 0 -2

Output:
8

"""

n, k = map(int, input().split())
arr = list(map(int, input().split()))

hashmap = {0 : 1}
pre_sum = 0
count = 0

for i in arr :
    pre_sum = pre_sum + i
    if (pre_sum - k) in hashmap :
        count = count + hashmap[pre_sum - k]

    hashmap[pre_sum] = hashmap.get(pre_sum, 0) + 1

print(count)