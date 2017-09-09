class adjacencyList:
    def __init__(self):
        self.adjList = {}
        
    def addEdge(self, source, dest):
        numSource = int(source)
        if numSource not in self.adjList:
            self.adjList[int(source)] = []
        self.adjList[numSource].append(int(dest))

    def findNeighbors(self, vertex, direction):
        neighbors = []
        if vertex in self.adjList:
            if direction == "backward":
                for i in range(len(self.adjList[vertex])-1,-1,-1):
                    neighbors.append(self.adjList[vertex][i])
            elif direction == "forward":
                for i in range(0, len(self.adjList[vertex])):
                    neighbors.append(self.adjList[vertex][i])
        return neighbors

    def numVertices(self):
        return len(self.adjList)
        
    def display(self):
        print("Adjacency List:")
        for elem in self.adjList:
            print("[" + str(elem) + "]=>" + str(self.adjList[elem]))
