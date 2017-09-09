from mystack import *

class dfs:
    def __init__(self, nv, aml):
        self.a = aml
        self.s = myStack()
        self.visited = [False] * nv
        self.order = []
        
    #DFS-recursive(G, s):
    #    mark s as visited 
    #    for all neighbours w of s in Graph G:
    #        if w is not visited:
    #            DFS-recursive(G, w)
    def searchRecursive(self, vertex):
        self.visited[vertex] = True
        self.order.append(vertex)
        neighbors = self.a.findNeighbors(vertex, "forward")
        for neighbor in neighbors:
            if not self.visited[neighbor]:
                self.searchRecursive(neighbor)
        return self.order

    #DFS-iterative (G, s):      //Where G is graph and s is source vertex
    #    S.push( s )            //Inserting s in stack 
    #    mark s as visited.
    #    while ( S is not empty):
    #       //Pop a vertex from stack to visit next
    #       v  =  S.top( )
    #       S.pop( )
    #       //Push all the neighbors of v in stack that are not visited   
    #       for all neighbours w of v in Graph G:
    #           if w is not visited :
    #               S.push( w )         
    #               mark w as visited
    def searchIterative(self, vertex):
        nodesVisited = []
        self.s.push(vertex)
        self.visited[vertex] = True
        while not self.s.empty():
            v = self.s.pop()
            nodesVisited.append(v)
            neighbors = self.a.findNeighbors(v, "backward")
            for neighbor in neighbors:
                if not self.visited[neighbor]:
                    self.s.push(neighbor)
                    self.visited[neighbor] = True
        return nodesVisited

