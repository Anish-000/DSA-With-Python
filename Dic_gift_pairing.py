"""
Question 1: “Gift Pairing”

Story:
A shop has n gift items, each with a price. 
A customer wants to buy exactly two different items whose prices add up to exactly T rupees. 
Two pairs count as different if they use different item positions, 
even when the prices are the same.
Find the number of such pairs.

Input Format:

Line 1: n T
Line 2: n integers, the prices

Output Format:

One integer, the number of valid pairs.

Constraints:

1 ≤ n ≤ 10^5
-1000 ≤ price ≤ 1000
-2000 ≤ T ≤ 2000

Test Cases:

Input: 5 6 / 1 5 3 3 3 → Output: 4
Input: 4 4 / 2 2 2 2 → Output: 6
Input: 3 10 / 1 2 3 → Output: 0
Input: 2 5 / 2 3 → Output: 1
Input: 6 0 / -1 1 0 0 2 -2 → Output: 3
Input: 5 7 / 3 4 3 4 7 → Output: 4
Input: 1 5 / 5 → Output: 0

"""

n, t = map(int, input().split())
arr = list(map(int, input().split()))

hashmap = {}
count = 0

for i in range(len(arr)):
    comp = t - arr[i]
    if comp in hashmap:
        count = count + hashmap[comp]

    hashmap[arr[i]] = hashmap.get(arr[i], 0) + 1

print(count)