from myqueue import *

class bfs:
    def __init__(self, nv, aml):
        self.a = aml
        self.q = myQueue()
        self.visited = [False] * nv
        print(self.visited)
        
    #BFS-iterative (G, s):      //Where G is graph and s is source vertex
    #    Q.push( s )            //Inserting s in stack 
    #    mark s as visited.
    #    while ( Q is not empty ):
    #        //Pop a vertex from stack to visit next
    #       v  =  Q.top( )
    #       Q.pop( )
    #       //Push all the neighbours of v in stack that are not visited   
    #       for all neighbours w of v in Graph G:
    #           if w is not visited :
    #               Q.push( w )         
    #               mark w as visited
    def search(self, vertex):
        nodesVisited = []
        self.q.push(vertex)
        self.visited[vertex] = True
        while not self.q.empty():
            v = self.q.pop()
            nodesVisited.append(v)
            neighbors = self.a.findNeighbors(v, "forward")
            print(neighbors)
            for neighbor in neighbors:
                if not self.visited[neighbor]:
                    self.q.push(neighbor)
                    self.visited[neighbor] = True
        return nodesVisited
