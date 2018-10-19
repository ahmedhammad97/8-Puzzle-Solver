#Imports
from .Node import Node
from time import time

try:
    from Queue import Queue, PriorityQueue  # versions < 3.0
except ImportError:
    from queue import Queue, PriorityQueue  # versions > 3.0



class Solution:
    def __init__(self, array):
        self.initialState = Node(array, "Start", None);


    def BFS(self):
        startTime = time()
        expanded = 0
        queue = Queue()
        visited = set()
        queue.put(self.initialState)

        while(not queue.empty()):
            front = queue.get()

            if front.grid in visited: #Visited Before
                continue

            #Processing
            if front.isGoal():
                path = front.backTrack()
                #self.drawGrids(path)
                self.processResult(path, front.cost, expanded, time()-startTime, "BFS")
                return path

            visited.add(front.grid)
            expanded+=1

            children = front.generateChildren() #Expanding
            for child in children:
                queue.put(child)

        return False


    def DFS(self):
        startTime = time()
        expanded = 0

        s = []
        visited = set()
        s.append(self.initialState)

        while(s):
            front = s.pop()

            if front.grid in visited: #Visited Before
                continue

            #Processing
            if front.isGoal():
                path = front.backTrack()
                #self.drawGrids(path)
                self.processResult(path, front.cost, expanded, time()-startTime, "DFS")
                return path

            visited.add(front.grid)
            expanded+=1

            children = front.generateChildren() #Expanding
            for child in children:
                s.append(child)

        return False



    def AStar(self, heuristic):
        startTime = time()
        expanded = 0
        PQueue = PriorityQueue()
        visited = set()
        PQueue.put((heuristic(self.initialState) ,self.initialState))

        while(not PQueue.empty()):
            front = (PQueue.get())[1]
            queueGrids.discard(front.grid)

            if front.grid in visited: #Visited Before
                continue

            #Processing
            if front.isGoal():
                path = front.backTrack()
                #self.drawGrids(path)
                self.processResult(path, front.cost, expanded, time()-startTime, "AStar-" + heuristic.__name__[:9])
                return path

            visited.add(front.grid)
            expanded+=1

            children = front.generateChildren() #Expanding
            for child in children:
                PQueue.put((heuristic(child) + child.cost, child))

        return False




    def processResult(self, path, cost, expanded, runtime, searchType):
        actions = []
        for x in path:
            actions.append(x.action)

        #Generate File
        f = open("./PuzzleSolver/solver/results/" + searchType + ".txt", "w")
        data = [
            "Actions : " + str(actions) + "\n",
            "Cost : " + str(cost) + "\n",
            "Nodes Expanded : " + str(expanded) + "\n",
            "Depth : " + str(len(actions)) + "\n",
            "Runtime : " + str(runtime) + "\n"
        ]
        f.writelines(data)
        f.close()

        return


    def drawGrids(self, path):
        for node in path:
            #Draw Grid
            for i in range(0,3):
                print (" ____________\n")
                print ("|", node.grid[i][0], "|", node.grid[i][1], "|", node.grid[i][2], "|")
            print (" ____________\n\n")
