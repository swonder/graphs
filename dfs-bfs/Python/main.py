from adjacencymatrix import *
from adjacencylist import *
from bfs import *
from dfs import *

def main():
    fileNames = ["graph1.txt", "graph2.txt", "graph3.txt", "graph4.txt", "graph5.txt"]
    file = open(fileNames[0], "r")

    i=0
    #Create adjacency matrix
    am = adjacencyMatrix()
    for line in file:
        if i == 0: #First row in file contains number 
            numVertices = int(line)
            am.create(numVertices)
        else:
            dest, source = line.split()
            am.addEdge(dest, source)
        i+=1
    am.display()
    
    '''
    i=0
    #Create adjacency list
    al = adjacencyList()
    for line in file:
        if i == 0: #First row in file contains number 
            numVertices = int(line)
        else:
            dest, source = line.split()
            al.addEdge(dest, source)
        i+=1
    al.display()
    '''
    
    #Searches
    d = dfs(numVertices, am)
    visited = d.searchRecursive(0)
    print(visited)

    '''
    d = dfs(numVertices, al)
    visited = d.searchIterative(0)
    print(visited)
        

    b = bfs(numVertices, am)
    visited = b.search(0)
    print(visited)    
    '''
    
if __name__ == "__main__":
    main()
