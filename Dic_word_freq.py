"""
Question 1: Dictionary/HashMap (Medium) — "Word Frequency Café"

Story:
Riya runs a small café and wants to display a "Today's Special Words" 
board based on customer reviews. 
She collects all the words from the reviews of the day (case-insensitive) and 
wants to find the word(s) that occurred the maximum number of times. If there is a tie, 
she wants them printed in alphabetical order, space-separated.

Only alphabetic characters count as part of a word — punctuation like ., ,, ! should be 
ignored/stripped.

Input Format:

A single string reviews containing multiple sentences (customer reviews concatenated with spaces).

Output Format:

The most frequent word(s), space-separated, in alphabetical order, all lowercase.

Constraints:

1 ≤ length of reviews ≤ 10^4
Reviews contain only letters, spaces, and punctuation (., ,, !, ?)

Test Cases:

Input: "The coffee is good. The coffee is hot!"
Output: the — wait, let's check: "the"=2, "coffee"=2, "is"=2, "good"=1, "hot"=1 → 
tie among coffee, is, the
Output: coffee is the
Input: "Best cafe ever, best coffee ever"
Output: best ever
(both occur twice; "coffee" and "cafe" occur once)
Input: "Amazing"
Output: amazing
Input: "Nice place. nice PLACE. Nice place!"
Output: nice place
(case-insensitive: both occur 3 times)
Edge case Input: "a a a b b c"
Output: a

"""

import string
n = input().lower()

for p in string.punctuation:
    n = n.replace(p, "")
    
words = n.split()
freq = {}

for i in words:
    if i not in freq:
        freq[i] = 0

    freq[i] = freq.get(i, 0) + 1

max_freq = max(freq.values())
res = []

for w in freq:
    if freq[w] == max_freq:
        res.append(w)

res = sorted(res)

print(*res)