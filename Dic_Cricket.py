"""
CRICKET STRIKE RATE ANALYZER
=============================

A local cricket league records every batter's performance ball-by-ball 
across multiple matches. The same player can bat in several different 
innings (records). You need to aggregate a player's TOTAL RUNS and 
TOTAL BALLS FACED across all their innings, then compute their overall 
Strike Rate and classify them.

Strike Rate Formula:
    Strike Rate = (Total Runs / Total Balls Faced) * 100

Classification Rules:
    Strike Rate >= 150            -> "Explosive Batter"
    Strike Rate >= 100 and < 150  -> "Steady Batter"
    Strike Rate < 100             -> "Slow Batter"

Special Case:
    If a player's TOTAL balls faced across all innings is 0, 
    print "No Data" instead of a strike rate and skip classification.

-----------------------------------------------------
INPUT FORMAT:
First line: N (number of innings records)
Next N lines: Name Runs BallsFaced

-----------------------------------------------------
OUTPUT FORMAT:
For each unique player (in the order they FIRST appeared in input), print:
Name TotalRuns TotalBalls StrikeRate Category

(Strike Rate must be rounded to exactly 2 decimal places)
If TotalBalls is 0, print:
Name TotalRuns TotalBalls No Data

-----------------------------------------------------
SAMPLE INPUT:
5
Virat 45 30
Rohit 20 25
Virat 55 20
Dhoni 10 15
Rohit 10 5

SAMPLE OUTPUT:
Virat 100 50 200.00 Explosive Batter
Rohit 30 30 100.00 Steady Batter
Dhoni 10 15 66.67 Slow Batter

-----------------------------------------------------
EXPLANATION OF SAMPLE:
- Virat has two innings: (45 runs,30 balls) and (55 runs,20 balls)
  Total = 100 runs, 50 balls -> SR = (100/50)*100 = 200.00 -> Explosive Batter
- Rohit has two innings: (20,25) and (10,5)
  Total = 30 runs, 30 balls -> SR = 100.00 -> exactly 100, falls under 
  "Steady Batter" since the rule is >=100 and <150
- Dhoni has one innings: (10,15)
  SR = (10/15)*100 = 66.67 -> Slow Batter

-----------------------------------------------------
CONSTRAINTS:
1 <= N <= 1000
0 <= Runs <= 500
0 <= BallsFaced <= 500
Name contains only alphabets, no spaces

-----------------------------------------------------
TEST CASES TO VALIDATE YOUR SOLUTION:

Test Case 1:
Input:
3
Sara 0 0
Aman 60 40
Sara 0 0

Output:
Sara 0 0 No Data
Aman 150 100 150.00 Explosive Batter


Test Case 2:
Input:
1
Kohli 149 100

Output:
Kohli 149 100 149.00 Steady Batter


Test Case 3:
Input:
4
Raina 30 20
Raina 20 10
Raina 25 25
Raina 100 25

Output:
Raina 175 80 218.75 Explosive Batter


Test Case 4:
Input:
2
Dhawan 99 100
Pant 100 100

Output:
Dhawan 99 100 99.00 Slow Batter
Pant 100 100 100.00 Steady Batter


Test Case 5:
Input:
6
Iyer 40 30
Jadeja 15 20
Iyer 20 10
Bumrah 5 10
Jadeja 5 5
Bumrah 0 0

Output:
Iyer 60 40 150.00 Explosive Batter
Jadeja 20 25 80.00 Slow Batter
Bumrah 5 10 50.00 Slow Batter

"""

n = int(input())
hashmap = {}
x = {}

for _ in range(n) :
    p = input().split()
    name = p[0]
    runs = int(p[1])
    balls = int(p[2])

    if name not in x :
        x[name] = []

    x[name].append((runs, balls))

for name in x :
    total_run = 0
    total_ball = 0
    sr = 0

    for runs, balls in x[name]:
        total_run = total_run + runs
        total_ball = total_ball + balls

        if total_ball > 0:
            sr = (total_run / total_ball) * 100

    hashmap[name] = ((total_run, total_ball, sr))

for name, (total_run, total_ball, sr) in hashmap.items():
    if sr >= 150 :
        print(name, total_run, total_ball, sr, "Explosive Batter")

    elif sr >= 100:
        print(name, total_run, total_ball, sr, "Steady Batter")

    elif sr > 0:
        print(name, total_run, total_ball, sr, "Slow Batter")

    else :
        print(name, total_run, total_ball, "No data")