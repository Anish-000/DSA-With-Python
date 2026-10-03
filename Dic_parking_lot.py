"""
Question A : "Parking Lot Sensor Log"

Story:
A parking lot's sensor logs n events in order. 
Each event is either a car entering (recorded as E) or a car leaving (recorded as L). 
The lot manager wants to know the length of the longest continuous stretch of events 
where the number of cars entering equals the number of cars leaving.

Input Format:

Line 1: n
Line 2: a string of n characters, each E or L

Output Format:

One integer, the length of the longest such stretch.

Constraints:

1 ≤ n ≤ 10^5

Test Cases (hand-verified):

Input: 6 / EELLEL → Output: 6
Input: 4 / EEEE → Output: 0
Input: 5 / ELEEL → Output: 4
Input: 1 / E → Output: 0
Input: 7 / ELELLEL → Output: 6
Input: 8 / EELEELLL → Output: 8

"""

n = int(input())
s = input()

hashmap = {0 : -1}
presum = 0
maxlen = 0

for i in range(n):
    if s[i] == 'E':
        presum = presum + 1

    else:
        presum = presum - 1

    if presum not in hashmap:
        hashmap[presum] = i

    maxlen = max(maxlen, (i - hashmap[presum]))

print(maxlen)