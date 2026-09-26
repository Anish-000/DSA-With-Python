"""
Question 3: Greedy (Easy) — "Vendor's Change Counter"

Story:
A street vendor named Sanjay only keeps coins of denominations {1, 2, 5, 10} 
(in his local currency). A customer wants change for amount X. 
Sanjay always wants to give the change using the minimum number of coins possible, 
and he has an unlimited supply of every denomination.

Find the minimum number of coins needed to make the exact amount X.

Input Format:

An integer X — the amount to be changed.

Output Format:

An integer — the minimum number of coins required.

Constraints:

1 ≤ X ≤ 10^6
Denominations available: 1, 2, 5, 10

Test Cases:

Input: X = 18
Output: 4
(10 + 5 + 2 + 1)
Input: X = 7
Output: 2
(5 + 2)
Input: X = 11
Output: 2
(10 + 1)
Input: X = 1
Output: 1
Edge case Input: X = 100
Output: 10
(all 10s)

"""

n = int(input())
arr = [10, 5, 2, 1]

rem_amount = n
coin_count = 0

for i in arr:
    if rem_amount > 0:
        coin_count = coin_count + (rem_amount // i)
        rem_amount = rem_amount % i

print(coin_count)