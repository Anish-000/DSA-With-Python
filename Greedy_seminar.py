"""
Question 2: “Seminar Hall Booking”

Story:
A college has a single seminar hall and receives n booking requests, 
each with a start time and an end time. The hall can host only one seminar at a time, 
but a seminar may start at exactly the time the previous one ends. 
The principal wants to accept as many requests as possible.
Find the maximum number of seminars that can be held.

Input Format:

Line 1: n
Next n lines: start end (requests are not in any particular order)

Output Format:

One integer, the maximum number of seminars.

Constraints:

1 ≤ n ≤ 10^5
0 ≤ start < end ≤ 10^9

Test Cases:

Input:
   3
   1 3
   2 4
   3 5

Output: 2

Input:
   4
   1 2
   3 4
   0 6
   5 7

Output: 3

Input:
   1
   2 9

Output: 1

Input:
   3
   1 10
   2 3
   4 5

Output: 2

Input:
   4
   1 4
   2 5
   3 6
   4 7

Output: 2

Input:
   5
   0 1
   1 2
   2 3
   3 4
   4 5

Output: 5

"""

n = int(input())
seminar = []

for _ in range(n) :
    p = input().split()
    start = int(p[0])
    end = int(p[1])

    seminar.append((start, end))

seminar.sort(key = lambda x : x[1])
total = 0
selected = []

for start, end in seminar:
    if start >= total:
        selected.append((start, end))
        total = end

print(len(selected))