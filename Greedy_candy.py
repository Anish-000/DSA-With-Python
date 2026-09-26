"""
Greedy Question (Easy) — "Teacher's Candy Distribution"

Story:
A kindergarten teacher, Mrs. Sen, has a basket of candies and 
a class of n children lined up for a snack break. 
Being fair, she wants to give each child at most one candy, 
but she only has a limited number of candies, m, in her basket.

Each child has a "hunger value" hunger[i] — the minimum size of candy 
that child needs to be satisfied. Mrs. Sen also has candies of various sizes, candy[j]. 
A child is satisfied only if they receive a candy whose size is greater than 
or equal to their hunger value.

Mrs. Sen wants to know: what is the maximum number of children she can satisfy, 
given her limited candies?

Input Format:

An integer n — number of children.
An array hunger[] of size n — hunger values of children.
An integer m — number of candies.
An array candy[] of size m — sizes of available candies.

Output Format:

An integer — the maximum number of children that can be satisfied.

Constraints:

1 ≤ n, m ≤ 1000
0 ≤ hunger[i], candy[j] ≤ 1000

Test Cases:

Input:
   hunger = [1, 2, 3]
   candy = [1, 1]

Output: 1
(Only one candy (size 1) can satisfy the child with hunger 1; 
the other size-1 candy can't satisfy anyone else since remaining hungers are 2 and 3)

Input:
   hunger = [1, 2]
   candy = [1, 2, 3]

Output: 2
(Candy of size 1 → child with hunger 1; candy of size 2 → child with hunger 2. Both satisfied.)

Input:
   hunger = [1, 2, 3]
   candy = [3]

Output: 1
(Only one candy, give it to the child needing the least (hunger 1) to save bigger candies... 
but here there's only 1 candy anyway, so 1 child satisfied)

Input:
   hunger = [10, 9, 8, 7]
   candy = [5, 6, 7, 8]

Output: 2
(Only candies of size 7 and 8 can satisfy hunger 7 and 8 respectively)

Edge case Input:
   hunger = [1, 1, 1]
   candy = [1, 1, 1]

Output: 3
(All hungers equal all candy sizes — everyone satisfied)

"""

n = int(input())
hunger = list(map(int, input().split()))

m = int(input())
candy = list(map(int,input().split()))

hunger.sort()
candy.sort()

i = 0
j = 0
count = 0

while i < n and j < m :
   if candy[j] >= hunger[i]:
      count = count + 1
      i = i + 1
      j = j + 1

   else:
      j = j + 1

print(count)
