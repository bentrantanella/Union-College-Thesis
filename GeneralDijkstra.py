import math
import random
import GraphADT
import AllQueueDS
import time
from resource import getrusage as resource_usage, RUSAGE_SELF


class Dijkstra:

    def __init__(self, graph, source, target):
        self.graph = graph
        self.source = source
        self.target = target

    def dijkstra(self, dataStruct):

        start_resources = resource_usage(RUSAGE_SELF)

        distList = [math.inf for i in range(0, self.graph.numVerts)]
        prevList = [-1 for i in range(0, self.graph.numVerts)]

        distList[self.source] = 0

        start_add_resources = resource_usage(RUSAGE_SELF)
        for i in range(0, self.graph.numVerts):
            dataStruct.add(i, distList)
        end_add_resources = resource_usage(RUSAGE_SELF)
        
        addTime = end_add_resources.ru_utime - start_add_resources.ru_utime
        addTime = "%.4f" % addTime

        getNextTime = 0
        updateTime = 0
        while dataStruct.size > 0:
            
            start_next_resources = resource_usage(RUSAGE_SELF)
            cur = dataStruct.getNext(self.graph, distList)
            end_next_resources = resource_usage(RUSAGE_SELF)
            
            getNextTime += (end_next_resources.ru_utime - start_next_resources.ru_utime)

            if cur == self.target:
                break
            

            for n in self.getNeighbors(cur):
                alt = distList[cur] + self.graph.getWeight(cur, n)
                if alt < distList[n]:
                    prev = distList[n]
                    distList[n] = alt
                    prevList[n] = cur
                    
                    start_up_resources = resource_usage(RUSAGE_SELF)
                    dataStruct.update(n, alt, distList, prev)
                    end_up_resources = resource_usage(RUSAGE_SELF)
                    
                    updateTime += (end_up_resources.ru_utime - start_up_resources.ru_utime)

        
        end_resources = resource_usage(RUSAGE_SELF)
        
        getNextTime = "%.4f" % getNextTime
        updateTime = "%.4f" % updateTime

        userTime = end_resources.ru_utime - start_resources.ru_utime
        userTime = "%.4f" % userTime
                
        return (distList, prevList, 0, userTime, addTime, getNextTime, updateTime)


        
    def getNeighbors(self, node):
        neighbors = []

        for i in range(self.graph.numVerts):
            if self.graph.getWeight(node, i) > 0:
                neighbors.append(i)
            
        return neighbors

    def shortestPath(self, prevList):
        spath = []
        u = self.target
        while u != -1:
            spath.insert(0, u)
            u = prevList[u]



        return spath
    
    
    