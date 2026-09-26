"""
Question 4: "Tech Fest Workshop Rooms"

Story:
A college tech fest has n workshops, each with a start time and an end time. 
A room can host only one workshop at a time, but if one workshop ends at time e, 
another may start in that same room at exactly time e.

The organizers want to book as few rooms as possible while still hosting every workshop.
Find the minimum number of rooms needed.

Input Format:
Line 1: n
Next n lines: start end

(Workshops are not given in sorted order.)

Output Format:
One integer, the minimum number of rooms required.

Constraints:
1 ≤ n ≤ 10^5
0 ≤ start < end ≤ 10^9

Test Cases:

Test Case 1:
Input:
3
0 30
5 10
15 20

Output:
2


Test Case 2:
Input:
3
7 10
2 4
4 6

Output:
1


Test Case 3:
Input:
5
1 3
3 5
5 7
2 6
6 8

Output:
2


Test Case 4:
Input:
4
1 5
2 6
3 7
4 8

Output:
4


Test Case 5:
Input:
1
3 9

Output:
1

"""

n = int(input())
starts = []
ends = []

for _ in range(n) :
    start , end = map(int, input().split())
    starts.append(start)
    ends.append(end)

starts.sort()
ends.sort()

i = 0
j = 0
rooms_need = 0
max_room = 0

while i < n :
    if starts[i] >= ends[j] :
        j = j + 1

    else:
        rooms_need = rooms_need + 1
    
    i = i + 1
    max_room = max(max_room, rooms_need)

print(max_room)
