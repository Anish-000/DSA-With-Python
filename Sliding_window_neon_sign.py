"""
Question 1: “Neon Sign Repair”

Story:
A shop has a row of n neon bulbs. Each bulb is either working (1) or faulty (0). 
The technician has time to replace at most one faulty bulb with a working one. 
After that, the owner wants the longest continuous stretch of working bulbs.
Find the length of that longest stretch.

Input Format:

Line 1: n
Line 2: n integers, each 0 or 1

Output Format:

One integer, the longest stretch of working bulbs after at most one replacement.

Constraints:

1 ≤ n ≤ 10^5

Test Cases:

Input: 8 / 1 1 0 1 1 1 0 1 → Output: 6
Input: 5 / 1 1 1 1 1 → Output: 5
Input: 4 / 0 0 0 0 → Output: 1
Input: 1 / 0 → Output: 1
Input: 6 / 1 0 1 0 1 0 → Output: 3
Input: 7 / 0 1 1 0 1 1 1 → Output: 6
Input: 2 / 1 0 → Output: 2

"""

n = int(input())
arr = list(map(int, input().split()))

left = 0
max_len = 0
count = 0

for right in range(n):
    if arr[right] == 0 :
        count = count + 1

    while count > 1:
        if arr[left] == 0:
            count = count - 1
        left = left + 1

    max_len = max(max_len, (right - left + 1))

print(max_len)