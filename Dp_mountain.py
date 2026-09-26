"""
THE MOUNTAIN CLIMBER

A climber wants to reach the top of a mountain with N checkpoints. 
At each checkpoint, the climber must pay an entry fee. 
The climber can start from either checkpoint 0 or checkpoint 1, 
and from any checkpoint can jump either 1 or 2 steps forward.

Find the minimum total fee to reach the last checkpoint.

INPUT FORMAT:

First line: N
Second line: N space-separated integers (fee at each checkpoint)

OUTPUT FORMAT:

Single integer -> Minimum fee to reach top

SAMPLE INPUT 1:

4
10 15 20 5

SAMPLE OUTPUT 1:

20

EXPLANATION:

Start at checkpoint 0 (fee=10)
Jump 2 → checkpoint 2 (fee=20)
Jump 2 → checkpoint 4? No, out of bounds!
Actually: 10 + 5 + ? 

dp[0]=10, dp[1]=15
dp[2]=min(10,15)+20=30
dp[3]=min(30,15)+5=20 ✅

SAMPLE INPUT 2:

3
1 100 1

SAMPLE OUTPUT 2:

2

SAMPLE INPUT 3:

1
5

SAMPLE OUTPUT 3:

5

"""

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * (n)
dp[0] = arr[0]
if len(arr) > 1:
    dp[1] = min(arr[0], arr[1])


for i in range(n) :
    if len(arr) > 1:
        dp[i] = min(dp[i - 1], dp[i - 2]) + arr[i]

    else:
        dp[i] = arr[i]

print(dp[n - 1])