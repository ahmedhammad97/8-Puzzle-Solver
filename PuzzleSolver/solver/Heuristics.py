def manhattanDistance(node):
    sum = 0
    for i in range(0,3):
        for j in range(0,3):
            row = node.grid[i][j] / 3
            col = node.grid[i][j] % 3

            sum+= (abs(i - row) + abs(j - col))
    return sum


def euclideanDistance(node):
    sum = 0
    for i in range(0,3):
        for j in range(0,3):
            row = node.grid[i][j] / 3
            col = node.grid[i][j] % 3

            sum+= pow( pow(i - row,2) + pow(j - col,2) , 0.5)
    return sum
