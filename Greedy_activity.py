"""
Given N activities with start and end times,
select maximum number of activities that 
don't overlap with each other.
(You can only do one activity at a time)

Input:
First line: N
Next N lines: ActivityName  StartTime  EndTime

Example Input:
4
A 1 3
B 2 5
C 4 6
D 5 8

Expected Output:
Selected: A C D
Count: 3

"""

n = int(input())
activity = []

for _ in range(n) :
    p = input().split()
    aname = p[0]
    start = int(p[1])
    end = int(p[2])

    activity.append((aname, start, end))

activity.sort(key = lambda x : x[2])
total = 0
selected = []

for name, start, end in activity:
    if start >= total:
        selected.append(name)
        total = end

print("Selected : ", *selected)
print("Count : ", len(selected))