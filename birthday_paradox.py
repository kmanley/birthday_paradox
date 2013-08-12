"""
Monte-carlo simulation that demonstrates the birthday paradox.
(See http://mathworld.wolfram.com/BirthdayProblem.html)
"""
import sys
import math
import random

def _trial(max_crowd_size=500):
    all_bdays = set()
    for num_people in xrange(1, max_crowd_size+1):
        this_bday = random.randint(1, 365 + (1 if random.randint(1,4)==4 else 0))
        if this_bday in all_bdays:
            return num_people
        else:
            all_bdays.add(this_bday)
            
def find_avg_crowd_size(trials):            
    total = 0
    for i in range(trials):
        total += _trial()
    avg = float(total) / trials
    print "avg size crowd needed for two people to share a birthday: %d people (%.2f)" % \
          (math.ceil(avg), avg)

def find_probability_given_crowd_size(crowd_size, trials):            
    total = 0
    for i in range(trials):
        result = _trial(crowd_size)
        total += (1 if result else 0)
    prob = float(total) / trials * 100.
    print "%.2f%% chance of shared birthday in crowd of %d" % (prob, crowd_size)
    
if __name__ == "__main__":
    find_avg_crowd_size(5000)
    for i in range(1, 76):
        find_probability_given_crowd_size(i, 5000)

            
