from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

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
                newGrid[i][j] = grid[(i*3)+j]

        if type == "bfs":
            #BFS Function
        elif type == "dfs":
            #DFS Function
        elif type == "astarM":
            #AStar Manhattan Function
        elif type == "astarE":
            #AStar Euclidean Function
        else:
            return HttpRequest("Failed :(")


        #return HttpResponse(request.POST['type'])
    else:
        return HttpRequest("Failed :(")
