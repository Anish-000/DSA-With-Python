"""
Question 2: “River Ferry”

Story:
A ferry service has n passengers waiting, each with a known weight. 
Every boat can carry at most two passengers at once, 
and the total weight on a boat must not exceed W. 
Every single passenger weighs at most W, so everyone can travel.
Find the minimum number of boats needed to carry everyone.

Input Format:

Line 1: n W
Line 2: n integers, the passenger weights

Output Format:

One integer, the minimum number of boats.

Constraints:

1 ≤ n ≤ 10^5
1 ≤ weight[i] ≤ W ≤ 10^9

Test Cases:

Input: 4 5 / 1 2 2 3 → Output: 2
Input: 4 3 / 3 2 2 1 → Output: 3
Input: 1 10 / 7 → Output: 1
Input: 5 100 / 50 50 50 50 50 → Output: 3
Input: 4 10 / 9 9 9 9 → Output: 4
Input: 6 6 / 1 2 3 4 5 5 → Output: 4
Input: 3 4 / 2 2 2 → Output: 2

"""

n, w = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
left = 0
right = n - 1
boats = 0

while left <= right:
    if left == right :
        boats = boats + 1
        left = left + 1
        right = right - 1

    elif arr[left] + arr[right] > w:
        boats = boats + 1
        right = right - 1

    elif arr[left] + arr[right] <= w :
        boats = boats + 1
        left = left + 1
        right = right - 1

print(boats)