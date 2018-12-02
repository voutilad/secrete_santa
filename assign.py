"""
Stupid logic for randomizing assignments. I use this once a year
so it'll stay messy and sloppy
"""
import os
import sys

def randInt():
    return int(os.urandom(1).hex(), 16)

NUM_PEOPLE = 18
assignments = {}
pool = []

for i in range(1, NUM_PEOPLE+1):
    assignments[i] = None
    pool.append(i)

for i in range(1, len(pool)+1):
    x = randInt() % len(pool)
    while i == pool[x]:
        x = randInt() % len(pool)
    pick = pool.pop(x)
    assignments[i] = pick

# sanity check
for key in assignments.keys():
    if key == assignments[key]:
        print("Integrity error: {key} == {assign}".format(key=key, assign=key))
        sys.exit(1)

for val in assignments.values():
    print(val)
