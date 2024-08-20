# multi source multi destination
# we can apply dijktra to all nodes and compute the answer but,
# if it has negative edges, dijtra cannot detect, it will go into endless loop
# using dijtra TC: V *E*logV

# floyd can detect negative cycles.
# using floyd TC: V**3

# concept: try to find best path for a source and destination, by travelling via all other nodes.

def floyd(matrix):
    n = len(matrix)

    for i in range(n):
        matrix[i][i] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    
    # if any negative cycle is there, then we may reach the source node with less than 0
    # ideally we have to reach source by 0 only

    for i in range(n):
        if matrix[i][i] < 0:
            print("negative cycle detected")
