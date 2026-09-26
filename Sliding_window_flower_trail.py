"""
Question 1: "Kavya's Flower Trail"

Story:
Kavya walks along a trail with n flower beds in a row, and each bed has a flower type ID. 
Her camera filter can lock onto at most k different flower types at once. 
She wants one continuous photo stretch, meaning consecutive beds, 
that contains at most k distinct types.

Find the longest such stretch.

Input Format:
Line 1: n k
Line 2: n integers representing flower type IDs

Output Format:
One integer — the maximum number of consecutive beds she can capture.

Constraints:
1 ≤ k ≤ n ≤ 10^5
1 ≤ type ID ≤ 10^9

Test Cases:

Test Case 1:
Input:
7 2
1 2 1 2 3 3 1

Output:
4

Explanation:
Beds 0 to 3 → 1 2 1 2 contain only 2 distinct flower types.


Test Case 2:
Input:
5 1
4 4 4 4 4

Output:
5


Test Case 3:
Input:
4 3
1 2 3 4

Output:
3


Test Case 4:
Input:
1 1
9

Output:
1


Test Case 5:
Input:
8 3
1 2 3 2 2 4 4 5

Output:
6

"""

n, k = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
max_len = 0
freq = {}

for right in range(n):
    if arr[right] not in freq:
        freq[arr[right]] = 0

    freq[arr[right]] += 1

    while len(freq) > k:
        freq[arr[left]] -= 1
        if freq[arr[left]] == 0:
            del freq[arr[left]]

        left = left + 1

    max_len = max(max_len, right - left + 1)

print(max_len)
