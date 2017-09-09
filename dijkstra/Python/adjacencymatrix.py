class adjacencyMatrix:
    def __init__(self):
        self.adjMatrix = []
        
    def create(self, vertices):
        for i in range(0, int(vertices)):
            self.adjMatrix.append([])
            for j in range(0, int(vertices)):
                self.adjMatrix[i].append(0)
            
    def addEdge(self, source, dest, dist):
        self.adjMatrix[int(source)][int(dest)] = dist
        
    #Returns a list with each element formatted as: [distance, (source, destination)] 
    def findNeighbors(self, vertex):
        neighbors = []
        for dest in range(0 ,len(self.adjMatrix[0])):
            for source in range(0, len(self.adjMatrix[0])):
                if source == vertex and int(self.adjMatrix[vertex][dest]) > 0:
                    neighbors.append([int(self.adjMatrix[vertex][dest]), (source, dest)])
        return neighbors
      
    def display(self):
        print('   ', end='')
            
        for i in range(0, len(self.adjMatrix)):
            print(str(i) + ' ', end='')
        print(" TO")
        j=0
        for row in self.adjMatrix:
            print(str(j) + '  ', end='') if j < 10 else print(str(j) + ' ', end='')
            k=0
            for elem in row:
                print(str(elem) + ' ', end='') if k < 10 else print(str(elem) + '  ', end='')
                k+=1
            j+=1
            print()
        print("FROM")
