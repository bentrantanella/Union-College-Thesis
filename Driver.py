import random
import GraphADT
import GeneralDijkstra
import AllQueueDS
import AllHeapDS

def SimpleTests():
    '''
    print('numVerts: ')
    numVerts = int(input())

    numEdges = 0

    while numEdges < (numVerts - 1) or numEdges > ((numVerts * (numVerts - 1)) / 2):
        print('numEdges: ')
        numEdges = int(input())
        if numEdges < (numVerts - 1) or numEdges > ((numVerts * (numVerts - 1)) / 2):
            print('Invalid number of edges')
    '''
    for i in range(10):
        numVerts = 12
        numEdges = 24
        
        g = GraphADT.GraphGenerator(numVerts, numEdges)

        g = g.createGraph()

        


        source = random.choice(range(0, numVerts))
        target = source

        while target == source:
            target = random.choice(range(0, numVerts))

        print('Source: ' + str(source))
        print('Target: ' + str(target))

        
        d = GeneralDijkstra.Dijkstra(g, source, target)

        pq = AllHeapDS.TwoThreeHeap()
        pqout = d.dijkstra(pq)
        print('Shortest path: ' + str(d.shortestPath(pqout[1])))
        #print('Time taken: ' + str(pqout[2]) + ' seconds')
        print('User time: ' + str(pqout[3]) + ' seconds')


if __name__ == '__main__':
    SimpleTests()

    
