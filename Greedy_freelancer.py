"""
FREELANCER TASK SCHEDULER
===========================

A freelancer receives N job offers. Each job has a DEADLINE (the last day 
by which it must be completed) and a PROFIT (money earned if completed 
on time). The freelancer can do ONLY ONE JOB PER DAY, and a job takes 
exactly 1 day to finish.

The freelancer wants to select a schedule of jobs (each on some day 
on or before its deadline, no two jobs on the same day) that 
MAXIMIZES TOTAL PROFIT.

Note: This is a different flavor of "interval scheduling" than picking 
non-overlapping activities — here you're not choosing time ranges, 
you're PLACING single-day jobs into slots before their deadlines, 
and every job has a value attached that affects your greedy choice.

-----------------------------------------------------
INPUT FORMAT:
First line: N (number of jobs)
Next N lines: JobName Deadline Profit

-----------------------------------------------------
OUTPUT FORMAT:
Line 1: Selected job names in the order they get scheduled (day 1, day 2, ...)
Line 2: Total Profit earned

-----------------------------------------------------
SAMPLE INPUT:
5
J1 2 100
J2 1 19
J3 2 27
J4 1 25
J5 3 15

SAMPLE OUTPUT:
Selected: J4 J1 J5
Total Profit: 140

-----------------------------------------------------
EXPLANATION OF SAMPLE:
Sort jobs by profit descending: J1(100), J3(27), J4(25), J2(19), J5(15)

Now greedily place each job on the LATEST free day <= its deadline:
- J1: deadline 2 -> place on day 2 (days: [_, J1])
- J3: deadline 2 -> day 2 taken, try day 1 -> free -> place J3 on day 1 
  (days: [J3, J1])
- J4: deadline 1 -> day 1 taken by J3, no earlier day available -> J4 REJECTED
- J2: deadline 1 -> day 1 taken -> REJECTED
- J5: deadline 3 -> day 3 free -> place on day 3 (days: [J3, J1, J5])

Wait — final schedule by day = J3(day1), J1(day2), J5(day3)
Total Profit = 27 + 100 + 15 = 142

(Trace this yourself with a dictionary {day: job} or a slot-array — 
this is a great exercise to catch greedy-placement bugs. Different 
tie-breaking or slot-filling order can change which job lands where 
when deadlines clash, so implement it carefully and compare with the 
test cases below.)

-----------------------------------------------------
CONSTRAINTS:
1 <= N <= 1000
1 <= Deadline <= N
1 <= Profit <= 10^4
Job names are unique strings

-----------------------------------------------------
INPUT-TAKING BRAINSTORM (think before coding):

This is a THREE-FIELD-PER-LINE input (name, deadline, profit) — similar 
shape to your activity selection question, but now think about how 
you'll STORE it for greedy processing:

1. List of tuples/dicts, then sort:
   jobs = []
   n = int(input())
   for _ in range(n):
       name, deadline, profit = input().split()
       jobs.append({"name": name, "deadline": int(deadline), "profit": int(profit)})
   jobs.sort(key=lambda x: -x["profit"])
   -> Clean and very readable; dictionary access makes code self-documenting.

2. Parallel lists / tuple sort (common in fast-typing exam settings):
   jobs = [tuple(input().split()) for _ in range(n)]
   jobs = [(name, int(d), int(p)) for name, d, p in jobs]
   jobs.sort(key=lambda x: -x[2])
   -> Faster to type under time pressure, but less readable — good to 
      practice both styles so you can pick based on time constraints.

3. Slot tracking — this is the TRICKY part of this problem. You need a 
   way to track which day-slots are filled. Two common techniques:
   a) A dictionary: slot = {} and check `if day not in slot`
   b) A fixed-size array: slot = [None] * (max_deadline + 1)
   Dictionary is more memory-efficient for sparse deadlines; array is 
   faster for lookups. Try implementing BOTH ways for this question — 
   it's a very common thing interviewers ask you to explain ("why did 
   you choose a dict here instead of an array?").

4. Edge case: what if TWO jobs have the SAME profit? Does your sort 
   need a secondary tie-breaker (e.g., earlier deadline first)? Check 
   Test Case 3 below to test this exact scenario.

-----------------------------------------------------
TEST CASES TO VALIDATE YOUR SOLUTION:

Test Case 1:
Input:
3
A 1 20
B 1 15
C 1 10

Output:
Selected: A
Total Profit: 20

Explanation: All three jobs have the SAME deadline (day 1), so only 
ONE job can ever be scheduled (only 1 slot exists on or before day 1). 
Greedy picks the highest profit job, A(20), and rejects B and C 
regardless of their profit — this tests whether your slot-search 
correctly stops looking once no valid day remains.


Test Case 2:
Input:
4
W 4 70
X 2 60
Y 4 50
Z 3 40

Output:
Selected: X Z W Y
Total Profit: 220

Explanation: Sorted by profit: W(70), X(60), Y(50), Z(40).
- W: deadline 4 -> place on day 4
- X: deadline 2 -> place on day 2
- Y: deadline 4 -> day4 taken, day3 free -> place on day 3
- Z: deadline 3 -> day3 taken, day2 taken, day1 free -> place on day 1
Final day order: day1=Z, day2=X, day3=Y, day4=W
Total = 70+60+50+40 = 220 (all 4 jobs fit since deadlines spread out 
across exactly 4 available days)


Test Case 3:
Input:
2
P1 1 50
P2 2 50

Output:
Selected: P2 P1
Total Profit: 100

(Tests equal-profit tie-breaking — both fit since deadlines differ)


Test Case 4:
Input:
1
Solo 1 999

Output:
Selected: Solo
Total Profit: 999


Test Case 5:
Input:
5
M1 2 10
M2 2 20
M3 2 30
M4 1 40
M5 1 50

Output:
Selected: M5 M3 M2
Total Profit: 100

Explanation: Only 2 slots exist total (max deadline = 2), so at most 
2 jobs can be scheduled — NOT 3. Recheck: with only days 1 and 2 
available, max 2 jobs fit. Trace this one very carefully — it's 
designed to test if your code correctly LIMITS scheduling to only 
as many jobs as there are available day-slots, not more.


Test Case 6:
Input:
6
T1 3 5
T2 1 6
T3 1 5
T4 2 4
T5 3 3
T6 2 8

Output:
Selected: T2 T6 T1
Total Profit: 19

"""

n = int(input())
freelance = []

for _ in range(n) :
    p = input().split()
    jname = p[0]
    deadline = int(p[1])
    profit = int(p[2])

    freelance.append((jname, deadline, profit))

freelance.sort(key = lambda x : x[2], reverse = True)
max_deadline = max(x[1] for x in freelance)
slot = [None] * (max_deadline + 1)
total = 0

for name, deadline, profit in freelance:
    for d in range(deadline, 0 , -1):
        if slot[d] is None:
            slot[d] = ((name, deadline, profit))
            total += profit
            break

selected = [slot[i][0] for i in range(len(slot)) if slot[i] is not None]
print("Selected : ", *selected)
print("Total Profit : ", total)