"""
Question: "Delivery Route Check"

Story:
A delivery company logs how the weight in a driver's van changes at each stop:
a positive number means packages were loaded, 
a negative number means packages were dropped off. 
The company wants to know, for the whole day's log of n stops, 
how many different continuous stretches of stops had a net change of exactly zero 
(meaning the same amount was loaded and dropped off across those stops).

Input Format:

Line 1: n
Line 2: n integers, the change at each stop (can be negative, positive, or zero)

Output Format:

One integer, the number of continuous stretches with a net change of exactly zero.

Constraints:

1 ≤ n ≤ 10^5
-1000 ≤ value ≤ 1000

Test Cases:

Input:
   5
   4 -4 3 -3 2

Output: 3

Input:
   4
   0 0 0 0

Output: 10

Input:
   3
   1 2 3

Output: 0

Input:
   1
   0

Output: 1

Input:
   6
   3 -1 -2 4 -4 0

Output: 6

Input:
   5
   5 -5 5 -5 5

Output: 6

"""

n = int(input())
arr = list(map(int, input().split()))

hashmap = {0 : 1}
presum = 0
count = 0

for i in arr :
    presum = presum + i
    if presum in hashmap:
        count = count + hashmap[presum]

    hashmap[presum] = hashmap.get(presum, 0) + 1

print(count)  