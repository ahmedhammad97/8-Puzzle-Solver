from copy import deepcopy

class Node:
    def __init__(self, grid, action, parent, cost=0):
        self.grid = grid
        self.action = action
        self.parent = parent
        self.cost = cost

    def __lt__(self, other): #Comparison fn used by PriorityQueue
        return 1



    def isGoal(self): #Checking for goal state
        for i in range(0,3):
            for j in range(0,3):
                if(self.grid[i][j] != (i*3+j)):
                    return False
        return True


    def generateChildren(self):
        zeroPos = None
        for i in range(0,3):
            for j in range(0,3):
                if self.grid[i][j] == 0:
                    zeroPos = [i,j]
                    break

        children = []

        if(zeroPos[0] + 1 < 3):
            #Swap with bottom
            newGrid = list(map(list, (deepcopy(self.grid))))
            newGrid[zeroPos[0]][zeroPos[1]] = newGrid[zeroPos[0] + 1][zeroPos[1]]
            newGrid[zeroPos[0] + 1][zeroPos[1]] = 0

            child = Node(tuple(tuple(i) for i in newGrid), "Down", self, self.cost + 1)
            children.append(child)


        if(zeroPos[1] + 1 < 3):
            #Swap with right
            newGrid = list(map(list, (deepcopy(self.grid))))
            newGrid[zeroPos[0]][zeroPos[1]] = newGrid[zeroPos[0]][zeroPos[1] + 1]
            newGrid[zeroPos[0]][zeroPos[1] + 1] = 0

            child = Node(tuple(tuple(i) for i in newGrid), "Right", self, self.cost + 1)
            children.append(child)


        if (zeroPos[0] - 1 >= 0):
            #Swap with top
            newGrid = list(map(list, (deepcopy(self.grid))))
            newGrid[zeroPos[0]][zeroPos[1]] = newGrid[zeroPos[0] - 1][zeroPos[1]]
            newGrid[zeroPos[0] - 1][zeroPos[1]] = 0

            child = Node(tuple(tuple(i) for i in newGrid), "Up", self, self.cost + 1)
            children.append(child)


        if(zeroPos[1] - 1 >= 0):
            #Swap with left
            newGrid = list(map(list, (deepcopy(self.grid))))
            newGrid[zeroPos[0]][zeroPos[1]] = newGrid[zeroPos[0]][zeroPos[1] - 1]
            newGrid[zeroPos[0]][zeroPos[1] - 1] = 0

            child = Node(tuple(tuple(i) for i in newGrid), "Left", self, self.cost + 1)
            children.append(child)


        return children


    def backTrack(self): #Marking Backward Path To Initial State
        track = []
        dummy = self
        while(dummy.parent != None):
            track.append(dummy)
            dummy = dummy.parent

        return track[::-1] #Reversed
