from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .solver import Solution, Heuristics

def index(request):
    return render(request, 'index.html')


def solve(request):
    if request.method == 'POST':
        grid = request.POST['grid']
        type = request.POST['type']

        grid = grid.split(',')

        newGrid = [[0 for x in range(3)] for y in range(3)]

        for i in range(0,3):
            for j in range(0,3):
                newGrid[i][j] = int(grid[(i*3)+j])

        gridTuple = tuple(tuple(i) for i in newGrid)
        problem = Solution.Solution(gridTuple)
        result = None

        if type == "bfs":
            result = problem.BFS()
        elif type == "dfs":
            result = problem.DFS()
        elif type == "astarM":
            result = problem.AStar(Heuristics.manhattanDistance)
        elif type == "astarE":
            result = problem.AStar(Heuristics.euclideanDistance)
        else:
            return HttpRequest("Failed :(")

        #Process result
        actions = []
        for node in result:
            actions.append(node.action)

        return HttpResponse(' '.join(actions))
    else:
        return HttpRequest("Failed :(")
