"""
Question 1: “Battery Drain Log”

Story:
A phone logs how much battery it used in each of n consecutive minutes, 
and every minute uses at least 1 unit. 
A tester wants to know the longest continuous stretch of minutes 
in which the total battery used is at most S units.
Find the length of that longest stretch. If even a single minute uses more than S, print 0.

Input Format:

Line 1: n S
Line 2: n integers, the battery used in each minute

Output Format:

One integer, the length of the longest valid stretch.

Constraints:

1 ≤ n ≤ 10^5
1 ≤ usage[i] ≤ 10^4
1 ≤ S ≤ 10^9

Test Cases:

Input: 6 8 / 3 1 2 1 1 4 → Output: 5
Input: 4 2 / 3 4 5 6 → Output: 0
Input: 1 5 / 5 → Output: 1
Input: 5 10 / 2 2 2 2 2 → Output: 5
Input: 7 7 / 4 1 1 1 5 1 1 → Output: 4
Input: 6 3 / 1 1 1 1 1 1 → Output: 3
Input: 5 6 / 5 1 1 1 5 → Output: 3

"""

n, s = map(int, input().split())
arr = list(map(int, input().split()))

maxlen = 0
left = 0
maxsum = 0
count = 0

for right in range(n) :
    maxsum = maxsum + arr[right]
    while maxsum > s:
        maxsum = maxsum - arr[left]
        left = left + 1

    maxlen = max(maxlen, (right - left + 1))

print(maxlen)