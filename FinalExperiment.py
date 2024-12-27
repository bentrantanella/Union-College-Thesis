import random
import GraphADT
import GeneralDijkstra
import AllQueueDS
import AllHeapDS
import csv
import time

def FinalExperiment():
    start = time.time()
    sizes = [1000,5000,10000]
    densities = [.01,.10,.20]
    dataStructs = [AllQueueDS.BucketQueue(), AllQueueDS.LLPriorityQueue(), AllQueueDS.PriorityQueue(), AllHeapDS.BinaryHeap()]
    fields = ['Data Structure','Number of Nodes','Density','User Time','Add Time','GetNext Time','Update Time']
    filename = "FinalExperiment.csv"
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)


    allData = []

    for size in sizes:
        print('Starting size ' + str(size))
        for density in densities:
            print('Starting density ' + str(density))
            #Number of graphs per combination of size and density
            for i in range(1,501):
                graph = GraphADT.GraphGenerator(size, density2edges(density, size))
                graph = graph.createGraph()
                source = random.choice(range(0, size))
                target = source
                while target == source:
                    target = random.choice(range(0, size))

                print("Graph made")
                
                dijkstra = GeneralDijkstra.Dijkstra(graph, source, target)

                #Number of data structs being tested
                for j in range(4):
                    dataStructs[j].reset()
                    out = dijkstra.dijkstra(dataStructs[j])
                    allData.append([dataStructs[j].name(), size, density, out[3], out[4], out[5], out[6]])
                    print(dataStructs[j].name() + " done")

                filename = "FinalExperiment.csv"
                with open(filename, 'a') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerows(allData)       
                allData = []
                print("Run done")
    
    end = time.time()
    print("Time taken: " + str(end-start))
    
def density2edges(density, numNodes):
    maxEdges = (numNodes * (numNodes - 1)) / 2
    return round((density * maxEdges))

if __name__ == '__main__':
    FinalExperiment()
                    