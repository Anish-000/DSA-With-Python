"""
Question A : "Signal Tower Readings"

Story:
A weather station records n hourly signal strength changes 
(can be positive or negative). Engineers want to know how many different continuous 
stretches of hours had a total change equal to a target value k.

Input Format:

Line 1: n k
Line 2: n integers

Output Format:

One integer, the count of continuous stretches summing to exactly k.

Constraints:

1 ≤ n ≤ 10^5
-1000 ≤ value ≤ 1000
-10^9 ≤ k ≤ 10^9

Test Cases (verified by hand):

Input: 5 5 / 1 2 3 -2 5 → Output: 2
Input: 3 3 / 3 3 3 → Output: 3
Input: 4 2 / 1 1 1 1 → Output: 3
Input: 1 5 / 5 → Output: 1
Input: 4 0 / 1 -1 1 -1 → Output: 4
Input: 5 2 / 2 -2 2 -2 2 → Output: 6

"""

n, k = map(int, input().split())
tower = list(map(int, input().split()))

hashmap = {0 : 1}
presum = 0
count = 0

for i in tower :
    presum = presum + i
    if (presum - k) in hashmap:
        count = count + hashmap[(presum - k)]

    hashmap[presum] = hashmap.get(presum, 0) + 1

print(count)