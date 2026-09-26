"""
THE CONCERT TICKET SYSTEM

A music festival sells tickets for N different shows. Each show has a name and ticket price. The same show can be purchased multiple times by different people.

At the end of the day, the manager wants a full sales report.

TASK: Find the following:

Total tickets sold for each show
Total revenue for each show
Most popular show (by tickets sold)
Most profitable show (by revenue)
Shows that generated revenue > 500

INPUT FORMAT:

First line: N (number of transactions)
Next N lines: ShowName  TicketPrice

SAMPLE INPUT:

8
RockBand 200
JazzNight 150
RockBand 200
Classical 300
JazzNight 150
RockBand 200
Classical 300
JazzNight 150

SAMPLE OUTPUT:

RockBand 3 600
JazzNight 3 450
Classical 2 600
Most Popular: RockBand
Most Profitable: RockBand
High Revenue: RockBand Classical

TEST CASES:

Test 1: N=1, single show → only that show in output
Test 2: All same show → one entry with all counts
Test 3: All different shows → each appears once

"""

n = int(input())
hashmap = {}
total = {}

for _ in range(n) :
    p = input().split()
    name = p[0]
    price = int(p[1])

    if name not in hashmap :
        hashmap[name] = 0
        total[name] = 0

    hashmap[name] = hashmap.get(name, 0) + price
    total[name] += 1

for i in hashmap:
    print(i, total[i], hashmap[i])

print("Most Popular : ", max(total, key = total.get))
print("Most Profitable : ", max(hashmap, key = hashmap.get))
print("High Revenue : ", end = " ")

for i in hashmap:
    if hashmap[i] > 500 :
        print(i, end = " ")
