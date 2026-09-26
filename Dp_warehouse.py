"""
Question: "Warehouse Crate Stacking"

Story:
A warehouse has n crates arranged in a row, each with a certain weight. 
A forklift operator wants to select some crates to load onto a truck to maximize total weight, 
but there's a rule: he can never select more than 2 crates in a row, 
AND additionally, the very first and very last crate in the row are considered adjacent 
to each other (the row is arranged in a circular loop inside the warehouse, 
since it wraps around a support pillar).
Find the maximum total weight the operator can load.

Input Format:

Line 1: n
Line 2: n integers — weight of each crate

Output Format:

Maximum total weight that can be loaded.

Constraints:

1 ≤ n ≤ 1000
0 ≤ weight[i] ≤ 10^4

Test Cases:

Input:
   4
   3 3 3 3

Output: 6

Input:
   5
   1 2 3 4 5

Output: 11

Input:
   1
   7

Output: 7

Input:
   2
   10 20

Output: 30

Input:
   6
   5 1 1 5 1 1

Output: 12

Input:
   3
   4 4 4

Output: 8

"""

n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(arr[0])

else :
    dp1 = [0] * (n - 1)
    dp2 = [0] * (n - 1)

    sub1 = arr[0 : n-1]
    sub2 = arr[1 : n]

    dp1[0] = sub1[0]

    if len(sub1) > 1:
        dp1[1] = sub1[0] + sub1[1]

    dp2[0] = sub2[0]
    if len(sub2) > 1:
        dp2[1] = sub2[0] + sub2[1]

    for i in range(2,len(sub1)):
        op1 = dp1[i - 1]
        op2 = sub1[i] + dp1[i - 2]
        if (i - 3) >= 0:
            op3 = sub1[i] + sub1[i - 1] + dp1[i - 3]

        else:
            op3 = sub1[i] + sub1[i - 1]

        dp1[i] = max(op1, op2, op3)

    for j in range(2, len(sub2)):
        op1 = dp2[j - 1]
        op2 = sub2[j] + dp2[j - 2]
        if (j - 3) >= 0:
            op3 = sub2[j] + sub2[j - 1] + dp2[j - 3]

        else:
            op3 = sub2[j] + sub2[j - 1]

        dp2[j] = max(op1, op2, op3)

    print(max(dp1[n - 2], dp2[n - 2]))
