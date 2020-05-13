import math
from EightPuzzle import * # manhattan distance, goal, and hvalue function added in eightpuzzle import math
import sys, random
from aStar import *


def hillclimbing(prob):
    current = prob.getStartState()
    current.printState()
    cv = hvalue(current)
    minvalue = cv

    while True:
        succs = prob.getSuccessors(current)
        cv = minvalue
        neighbor = None
        for succ in succs:
            hv = hvalue(succ[0])
            if hv < minvalue:
                minvalue = hv
                neighbor = succ[0]
        print("minvalue is ", minvalue, "cv is ", cv)
        if minvalue >= cv:
            return current
        current = neighbor

def if_(test, result, alternative):
    if test:
        return result
    else:
        return alternative

schedule = lambda t: if_(t < 1000, 800 * math.exp(-0.005 * t), 0)

def simulated_annealing(prob):
    current=prob.getStartState()
    for t in xrange(sys.maxint):
        T=schedule(t)
        #print "T value is ",T
        if T==0:
            return current
        current.printState()
        succs= prob.getSuccessors(current)
        next = random.choice(succs)
        delta_e = hvalue(next[0])-hvalue(current)
        if delta_e < 0 or probability(math.exp(delta_e/T)):
            current=next[0]

def probability(p):
    return p > random.uniform(0.0,1.0)

#xxxxxxxxxxxxxx

state=PuzzleState([1,2,3,4,0,5,6,7,8])
prob=SearchProblem(state)
s=hillclimbing(prob)
s.printState()

#xxxxxxxxxxxx

for t in range(10):
    print(schedule(t))

#xxxxxxxxxxxxxx

state=PuzzleState([1,2,3,4,0,5,6,7,8])
prob=SearchProblem(state)
s=simulated_annealing(prob)
s.printState()