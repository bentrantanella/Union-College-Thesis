import random
import GeneralDijkstra
import AllQueueDS

class GraphADT:

    def __init__(self, numVerts, numEdges):
        self.numVerts = numVerts
        self.numEdges = numEdges
        self.adjMatrix = [[0 for c in range(numVerts)]
                          for r in range(numVerts)]
        
        self.curEdges = 0

    def __str__(self):
        out = ''

        for r in range(self.numVerts):
            out += str(self.adjMatrix[r]) + '\n'
        
        return out
    
    def setWeight(self, v1, v2, weight):
        self.adjMatrix[v1][v2] = weight
        self.adjMatrix[v2][v1] = weight
        self.curEdges += 1
    
    def getWeight(self, v1, v2):
        return self.adjMatrix[v1][v2]


class GraphGenerator:

    def __init__(self, numVerts, numEdges):
        self.numVerts = numVerts
        self.numEdges = numEdges

    def createGraph(self):
        g = GraphADT(self.numVerts, self.numEdges)
        unvisited = []
        for i in range(g.numVerts):
            unvisited.append(i)
        visited = []

        current = random.choice(unvisited)
        unvisited.remove(current)
        visited.append(current)

        while len(unvisited) > 0:
            next = random.choice(unvisited)

            g.setWeight(current, next, random.randint(1, 100))

            visited.append(next)
            unvisited.remove(next)

            current = random.choice(visited)
        while g.curEdges < g.numEdges:
            v1 = random.choice(visited)
            v2 = random.choice(visited)

            if v1 != v2 and g.adjMatrix[v1][v2] == 0:
                g.setWeight(v1, v2, random.randint(1, 100))
        return g
    


        

        

    