"""
Question 1: “Conveyor Belt Scanner”

Story:
A factory conveyor belt carries n items in a row, 
and each item has a product code written as a lowercase letter. 
A quality inspector watches a continuous stretch of items and 
gets confused if the same code appears twice in his view.
Find the length of the longest continuous stretch of items in which no code repeats.

Input Format:

Line 1: n
Line 2: a string of n lowercase letters

Output Format:

One integer, the length of the longest stretch with no repeated code.

Constraints:

1 ≤ n ≤ 10^5

Test Cases:

Input: 8 / abcabcbb → Output: 3
Input: 5 / bbbbb → Output: 1
Input: 6 / pwwkew → Output: 3
Input: 1 / a → Output: 1
Input: 6 / abcdef → Output: 6
Input: 4 / dvdf → Output: 3
Input: 4 / abba → Output: 2

"""

n = int(input())
s = input()
left = 0
max_len = 0
code = {}

for right in range(n):
    if s[right] not in code:
        code[s[right]] = 0

    code[s[right]] = code.get(s[right], 0) + 1

    while code[s[right]] > 1:
        code[s[left]] -= 1
        left = left + 1

    max_len = max(max_len, (right - left + 1))

print(max_len)