from pip._vendor.distlib.compat import raw_input

from EightPuzzle import *
import heapq
class PriorityQueue:
    def __init__(self):
        # print "initialize with something"
        self.heap = []

    def printQueue(self):
        # print "print the current status of queue"
        print (self.heap)

    def push(self, item, value):
        # print "push item in the queue with respect to value/priority"
        entry = (value, item)
        heapq.heappush(self.heap, entry)

    def pop(self):
        # print "return the item with least value"
        (value, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        # print "return if the queue is empty or not"
        return len(self.heap) == 0

    def update(self, item, value):
        # print "update the item with new value"
        for index, (v, i) in enumerate(self.heap):
            if i[0] == item[0]:
                if v <= value:
                    break
                else:
                    del self.heap[index]
                    self.heap.append((value, item))
                    heapq.heapify(self.heap)  # sorting
                    break
            else:
                self.push(item, value)

def mdistance(xy1, xy2):
        return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

goal = {0:(0, 0), 1:(0, 1), 2:(0,2), 3:(1, 0), 4:(1, 1), 5:(1, 2), 6:(2, 0), 7:(2, 1), 8:(2, 2)}
print(goal[0])

def hvalue(state):
        hscore = 0

        for row in range(3):
            for col in range(3):
                if state.cells[row][col] == 0:
                    continue
                goal1 = goal[state.cells[row][col]]
                xy1 = (row, col)
                hscore += mdistance(xy1, goal1)
        return hscore

import copy
def Astar(problem):
        state = problem.getStartState()

        queue = PriorityQueue()
        action = ""
        fPath = []
        visitedStates = []
        priority = 999
        queue.push(((state, action), fPath), priority)
        i = 0
        while queue.isEmpty() == False:

            #print(i+1)
            #raw_input("Please Enter")
            queue.printQueue()
            current = queue.pop()
            cStatewithaction = current[0]
            cPath = current[1]
            cState = cStatewithaction[0]
            cAction = cStatewithaction[1]
            if cState in visitedStates:

                continue
            else:

                visitedStates.append(cState)
            if problem.isGoalState(cState):

                return cPath
            else:

                succs = problem.getSuccessors(cState)
                for succ in succs:

                    sPath = copy.deepcopy(cPath)
                    if succ[0] in visitedStates:

                        continue
                    else:

                        sPath.append(succ[1])
                        # hv
                        hv = hvalue(succ[0])
                        # gv
                        gv = len(sPath)
                        queue.update((succ, sPath), gv + hv)


#xxxxxxxxxxxxxx

p = PuzzleState([1,2,3,0,4,5,6,7,8])
print(hvalue(p))
prob = SearchProblem(p)
print(prob)
path = Astar(prob)
print(path)