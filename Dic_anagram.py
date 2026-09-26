"""
Dictionary Question (Medium) — "Library Anagram Shelves"

Story:
Meera works at a library that's reorganizing its ancient scroll collection. 
Two scrolls are considered to belong on the same shelf 
if the words written on them are anagrams of each other 
(same letters, rearranged — case-insensitive, ignore spaces).

Given a list of n scroll titles, group them into shelves. For each shelf, 
the scrolls should be printed in the order they first appeared in the input. 
The shelves themselves should be printed in the order their first scroll appeared in the input. 
Each shelf's scrolls go on one line, space-separated.

Input Format:

An integer n — number of scrolls.
n lines, each containing one scroll title (a single word or a short phrase, letters and spaces only).

Output Format:

Each shelf (group of anagram scrolls) printed on its own line, space-separated, 
scrolls in original input order, shelves in order of first appearance.

Constraints:

1 ≤ n ≤ 1000
Each title has 1 ≤ length ≤ 50, letters and spaces only

Test Case 1:

Input:
   5
   eat
   tea
   tan
   ate
   nat

Output:

   eat tea ate
   tan nat

Tes Case 2:

Input:
   4
   listen
   silent
   hello
   world

Output:

   listen silent
   hello
   world

Test Case 3 :

Input:
   3
   Rat
   Tar
   Art

Output:

   Rat Tar Art

(case-insensitive matching, but original casing is preserved in output)

Test Case 4 :

Input:
   1
   apple

Output:

   apple

Test Case 5:

Edge case Input:
   4
   listen
   inlets
   banana
   Silent

Output:

   listen inlets Silent
   banana

"""

n = int(input())
hashmap = {}

for _ in range(n):
    p = input()
    sorted_key = "".join(sorted(p))

    if sorted_key not in hashmap:
        hashmap[sorted_key] = p

    else:
        hashmap[sorted_key] = hashmap[sorted_key] + " " + p

for key in hashmap:
    print(hashmap[key])