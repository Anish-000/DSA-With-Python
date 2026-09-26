"""
THE ADVENTURER'S GUILD

An adventurer has received N quest offers from the Guild. 
Each quest has a deadline (in days) and a reward (in gold). 
The adventurer can only complete ONE quest per day. 
Once a quest's deadline passes, it cannot be completed.

The adventurer wants to MAXIMIZE total gold earned.

INPUT FORMAT:

First line: N (number of quests)
Next N lines: QuestName  Deadline  Reward

OUTPUT FORMAT:

Selected quests (in slot order)
Maximum Gold earned

SAMPLE INPUT 1:

5
DragonSlaying 2 500
TreasureHunt 1 300
GoblinRaid 2 400
WolfHunt 1 100
DungeonClear 3 600

SAMPLE OUTPUT 1:

Selected: DungeonClear TreasureHunt DragonSlaying
Max Gold: 1400

SAMPLE INPUT 2:

3
QuestA 1 100
QuestB 1 200
QuestC 1 150

SAMPLE OUTPUT 2:

Selected: QuestB
Max Gold: 200

SAMPLE INPUT 3:

1
SingleQuest 1 999

SAMPLE OUTPUT 3:

Selected: SingleQuest
Max Gold: 999

CONSTRAINTS:

1 <= N <= 10^5
1 <= Deadline <= N
1 <= Reward <= 10^4

"""

n = int(input())
adv = []

for _ in range(n) :
    p = input().split()
    qname = p[0]
    deadline = int(p[1])
    reward = int(p[2])

    adv.append((qname, deadline, reward))

adv.sort(key = lambda x : x[2], reverse = True)
max_deadline = max(x[1] for x in adv)
slot = [None] * (max_deadline + 1)
total = 0

for name, deadline, reward in adv:
    for d in range(deadline, 0, -1):
        if slot[d] is None:
            slot[d] = ((name, deadline, reward))
            total += reward
            break

selected = [slot[i][0] for i in range(len(slot)) if slot[i] is not None]
print("Selected : ", *selected)
print("Max Gold : ", total)