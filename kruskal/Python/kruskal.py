class kruskal:
    def __init__(self, e):
        self.edges = e
        self.sets = []
        
    #Format for nodes of tree [key, parent, rank]
    def makeSet(self, x):
        if x not in self.sets:
            self.sets.append([x, None, 0])

    def find(self, x):
        parent = []
        for s in self.sets:
            if s[0] == x:
                #Element found - walk up the tree and return root node
                parent = s
                while parent[1] != None:
                    parent = self.find(parent[1])
        return parent
            
    def union(self, x, y):
        nodeX = self.find(x)
        nodeY = self.find(y)
        if nodeX[0] == nodeY[0]:
            return
        #Set the root node of x to node y
        if nodeX[2] > nodeY[2]:
            for i in range(0, len(self.sets)):
                if self.sets[i][0] == nodeY[0]:
                    self.sets[i][1] = nodeX[0]
        #Set the root node of y to node x
        else:
            for i in range(0, len(self.sets)):
                if self.sets[i][0] == nodeX[0]:
                    self.sets[i][1] = nodeY[0]
                    #Increment rank 
                    if nodeX[2] == nodeY[2]:
                        for j in range(0, len(self.sets)):
                            if self.sets[j][0] == nodeY[0]:
                                self.sets[j][2] += 1

    def run(self):
        for edge in self.edges:
            self.makeSet(edge[0])
            self.makeSet(edge[1])

        #Sort egdes by distance
        self.edges = sorted(self.edges, key=lambda l:l[2])

        mst = []
        for edge in self.edges:
            if self.find(edge[0]) != self.find(edge[1]):
                mst.append(edge)
                self.union(edge[0], edge[1])
        return mst
