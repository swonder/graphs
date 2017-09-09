import math
from adjacencymatrix import *
from dijkstra import *

def main():
    #Sample graph files
    fileNames = ["graph1.txt", "graph2.txt", "graph3.txt"]
    file = open(fileNames[2], "r")

    #---Format of files---
    #First row in file contains number of nodes in graph
    #Rows after first row contain edge info.
    #Format: start node, end node, distance
    #Example: 0 3 5 = Edge that goes from vertex 0 to 3 with distance 5   

    #Populate an adjacency matrix from file
    am = adjacencyMatrix()
    i=0
    for line in file:
        if i == 0: 
            numVertices = int(line)
            am.create(numVertices)
        else:      
            dest, source, dist = line.split()
            dest, source, dist = int(dest), int(source), int(dist)
            am.addEdge(dest, source, dist)
        i+=1
        
    #Run Dijkstra's shortest path algorithm on graph    
    d = dijkstra(am, numVertices)
    d.run(0)
    d.displaySolution()

if __name__ == '__main__':    
    main()
