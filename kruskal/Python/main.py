from kruskal import kruskal
    
def main():
    edges = []
    files = ["graph1.txt", "graph2.txt"]
    file = open(files[0], 'r')
    #Format of each line in file: vertex1 vertex2 distance
    for line in file:
        v1, v2, dist = line.split()    
        edges.append([v1, v2, int(dist)])
    file.close()
    print("Edges of graph: " + str(edges))

    k = kruskal(edges)
    mst = k.run()
    print("Minimum spanning tree for graph: " +str(mst))
    
if __name__ == '__main__':
    main()
