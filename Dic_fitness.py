"""
Question: "Fitness Streak"

Story:
A fitness app records the day numbers on which a user completed a workout. 
The records are stored in no particular order, 
and the same day number may appear more than once because of sync glitches. 
The app wants to reward the user's longest streak, 
meaning the largest set of day numbers that follow one another with no gaps 
(like days 4, 5, 6, 7).

Find the length of the longest streak.

Input Format:

Line 1: n
Line 2: n integers, the recorded day numbers

Output Format:

One integer, the length of the longest streak.

Constraints:

1 ≤ n ≤ 10^5
1 ≤ day number ≤ 10^9

Test Cases:

Input:
   6
   100 4 200 1 3 2

Output: 4

Input:
   5
   5 5 5 5 5

Output: 1

Input:
   1
   42

Output: 1

Input:
   7
   10 5 12 3 55 30 4

Output: 3

Input:
   8
   9 1 4 7 3 2 8 5

Output: 5

Input:
   5
   1000000000 999999999 1 999999998 2

Output: 3

"""

n = int(input())
arr = list(map(int, input().split()))
current = 1
best = 1

final_arr = list(set(arr))
final_arr.sort()

if len(final_arr) == 1:
    print("1")

else:
    for i in range(len(final_arr) - 1) :
        if final_arr[i + 1] == final_arr[i] + 1:
            current = current + 1

        else:
            current = 1

        best = max(best, current)
    
    print(best)