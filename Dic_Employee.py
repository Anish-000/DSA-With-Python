'''
A company tracks employee login and logout times.
Calculate the total hours worked by each employee
and check if they completed their shift.

Rules:
  Working hours >= 8   → "Full Shift"
  Working hours >= 4   → "Half Shift"
  Working hours < 4    → "Absent"

Input:
First line: N (number of records)
Next N lines: Name  LoginHour  LogoutHour

Example Input:
4
Rahul 9 17
Priya 10 14
Arjun 8 16
Priya 6 9

Note: Same employee can have multiple records
(like Priya above) — add their hours together!

Expected Output:
Rahul 8 Full Shift
Priya 7 Half Shift
Arjun 8 Full Shift

'''

n = int(input())
hashmap = {}

for _ in range(n) :
    p = input().split()
    name = p[0]
    login = int(p[1])
    logout = int(p[2])

    worktime = logout - login

    if name not in hashmap:
        hashmap[name] = 0

    hashmap[name] = hashmap.get(name, 0) + worktime

for name, total in hashmap.items():
    if total >= 8:
        print(name, total, "Full Shift")

    elif total >= 4:
        print(name, total, "Half Shift")

    else:
        print(name, total, "Absent")