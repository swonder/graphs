class adjacencyMatrix:
    def __init__(self):
        self.adjMatrix = []
    
    def create(self, vertices):
        for i in range(0, int(vertices)):
            self.adjMatrix.append([])
            for j in range(0, int(vertices)):
                self.adjMatrix[i].append(0)
            
    def addEdge(self, source, dest):
        self.adjMatrix[int(source)][int(dest)] = 1

    def findNeighbors(self, vertex, direction):
        neighbors = []
        if direction == "backward":
            for i in range(len(self.adjMatrix[0])-1, -1, -1):
                if self.adjMatrix[vertex][i] == 1:
                    neighbors.append(i)
        elif direction == "forward":
            for i in range(0, len(self.adjMatrix[0])):
                if self.adjMatrix[vertex][i] == 1:
                    neighbors.append(i)
        return neighbors    

    def numVertices(self):
        return len(self.adjMatrix)+1
        
    def display(self):
        print('   ', end='')
            
        for i in range(0, len(self.adjMatrix)):
            print(str(i) + ' ', end='')
        print(" TO")
        j=0
        for row in self.adjMatrix:
            print(str(j) + '  ', end='') if j<10 else print(str(j) + ' ', end='')
            k=0
            for elem in row:
                print(str(elem) + ' ', end='') if k < 10 else print(str(elem) + '  ', end='')
                k+=1
            j+=1
            print()
        print("FROM")
