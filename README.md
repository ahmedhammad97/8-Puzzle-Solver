# 8-Puzzle-Solver
![ScreenShot](https://github.com/ahmedhammad97/8-Puzzle-Solver/blob/master/screenVideo.gif)

## How it works
When the user clicks the "Solve" button, the client verify the validity of the input sequence, and sends it to the server, along with the searching algorithm chosen, using an Ajax request.

The server, which has Django running on, converts the received data into Python-like format, and passes it to the Solution class, where the real artificial intelligence comes into the game.

After finding the goal state, a backtrack function is called to collect the desired data, and return it to the controllers, which themselves 'stringify' it and responds it back to the client.

The client then starts rendering the grid, and doing a move every 1 second, until the list of actions received is finished.


## List of Algorithms supported:
- Breadth First Search
- Depth First Search
- A* with 'Manhattan distance' heuristic
- A* with 'Euclidean distance' heuristic
