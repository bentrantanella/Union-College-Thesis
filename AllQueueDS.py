import GraphADT
import GeneralDijkstra
import math
import numpy as np

class LLPriorityQueue:

    def __init__(self):
        self.queue = DLinkedList()
        self.size = 0
    
    def __str__(self):
        if self.size == 0:
            return "Empty queue"
        return str(self.queue)

    def size(self):
        return self.size
    
    def name(self):
        return 'LL Priority Queue'
    
    def reset(self):
        self.queue = DLinkedList()
        self.size = 0

    def add(self, node, distList):
        n = DLinkedListNode([node, distList[node]], None, None)

        if self.queue.head == None:
            self.queue.head = n
            self.size += 1
            #print(str(self.queue))
            #print("1")
            return
        
        if self.queue.tail == None:
            if self.queue.head.val[1] <= distList[node]:
                self.queue.head.next = n
                n.prev = self.queue.head
                self.queue.tail = n
            else:
                self.queue.head.prev = n
                n.next = self.queue.head
                self.queue.tail = self.queue.head
                self.queue.head = n
                
            self.size += 1
            #print(str(self.queue))
            #print("2")
            return
        
        if self.queue.head.val[1] > distList[node]:
            self.queue.insertAtHead(n)
            self.size += 1
            #print(str(self.queue))
            #print("3")
            return
        
        if self.queue.tail.val[1] <= distList[node]:
            self.queue.insertAtTail(n)
            self.size += 1
            #print(str(self.queue))
            #print("4")
            return
        
        self.queue.insertInOrder(n)
        self.size += 1
        #print(str(self.queue))
        #print("5")
        return
    
    def getNext(self, graph, distList):
        out = self.queue.head
        #print(str(self.queue))
        if self.queue.head.next == None:
            self.queue.head = None
            return out.val[0]
        
        self.queue.head = self.queue.head.next
        self.queue.head.prev = None
        self.size -= 1
        return out.val[0]
    
    def update(self, node, alt, distList, prev):
        if self.queue.head.next == None:
            self.queue.head.val[1] = alt
            #print(str(self.queue))
            return
    
        frunner = self.queue.head
        brunner = self.queue.tail

        while frunner.val[1] <= brunner.val[1]:
            if frunner.val[0] == node:
                self.reOrder(frunner, distList)
                #print(str(self.queue))
                return
            if brunner.val[0] == node:
                self.reOrder(brunner, distList)
                #print(str(self.queue))
                return
            
            frunner = frunner.next
            brunner = brunner.prev
        #print(str(self.queue))


        return
    
    def reOrder(self, n, distList):
        if n == self.queue.head:
            self.queue.head = self.queue.head.next
            self.queue.head.prev = None
            n.next = None

            self.add(n.val[0], distList)
            return
        
        if n == self.queue.tail:
            self.queue.tail = self.queue.tail.prev
            self.queue.tail.next = None
            n.prev = None

            self.add(n.val[0], distList)
            return
        
        n.prev.next = n.next
        n.next.prev = n.prev
        n.next = None
        n.prev = None

        self.add(n.val[0], distList)

        return



    
class DLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        toReturn = ""
        runner = self.head
        while runner != None:
            toReturn += str(runner) + ", "
            runner = runner.next
    
        return toReturn
    
    def popHead(self):
        toReturn = self.head

        if self.head.next == None:
            self.head = None
            self.size -= 1
            return toReturn
        
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        return toReturn
    
    def popN(self, val):
        if self.head.val == val:
            return self.popHead()
        
        if self.tail.val == val:
            toReturn = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return toReturn

        hrunner = self.head
        trunner = self.tail

        while hrunner.val != val and trunner.val != val:                
            hrunner = hrunner.next
            trunner = trunner.prev

        if hrunner.val == val:
            toReturn = hrunner
            hrunner.prev.next = hrunner.next
            hrunner.next.prev = hrunner.prev
            self.size -= 1
            return hrunner
        
        if trunner.val == val:
            toReturn = trunner
            trunner.prev.next = trunner.next
            trunner.next.prev = trunner.prev
            self.size -= 1
            return trunner
        
        print('Not found')
        return None

    
    def insertAtHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
            return
        temp = self.head
        self.head = node
        self.head.next = temp
        self.head.next.prev = node
        self.size += 1
        return

    def insertAtTail(self, node):
        if self.head is None:
            self.insertAtHead(node)
            return
        
        if self.tail == self.head or self.tail is None:
            self.tail = node
            self.tail.prev = self.head
            self.head.next = self.tail
            self.size += 1
            return

        temp = self.tail
        self.tail = node
        self.tail.prev = temp
        self.tail.prev.next = node
        self.size += 1
        return

    def insertInOrder(self, node):
        frunner = self.head
        brunner = self.tail
        wasInserted = False
        #print(self.__str__())
        #print(node.val[1])
        while not wasInserted:
            if frunner.val[1] > node.val[1]:
                frunner.prev.next = node
                node.prev = frunner.prev
                node.next = frunner
                frunner.prev = node
                wasInserted = True
            elif brunner.val[1] < node.val[1]:
                brunner.next.prev = node
                node.next = brunner.next
                node.prev = brunner
                brunner.next = node
                wasInserted = True

            frunner = frunner.next
            brunner = brunner.prev
        
        self.size += 1
        #print(self.__str__() + '\n')
        return
                

class DLinkedListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):

        toReturn = "(" + str(self.val[0]) + ", " + str(self.val[1])
        if self.next != None:
            toReturn += ", " + str(self.next.val[0])
        else:
            toReturn += ", None"
        
        if self.prev != None:
            toReturn += ", " + str(self.prev.val[0])
        else:
            toReturn += ", None"
        
        toReturn += ")"

        return toReturn

class BucketQueue:
    def __init__(self):
        self.array = np.array([DLinkedList()])
        self.size = 0
        
    def name(self):
        return 'Bucket Queue'
    
    def reset(self):
        self.array = np.array([DLinkedList()])
        self.size = 0

    def add(self, node, distList):
        if distList[node] == math.inf:
            self.array[0].insertAtTail(DLinkedListNode(node, None, None))
            self.size += 1
            return
        
        if len(self.array) == 1 and distList[node] == 0:
            newArr = np.array([DLinkedList()])
            self.array = np.concatenate((self.array, newArr))

        if len(self.array) - 1 <= distList[node]:
            dif = distList[node] - (len(self.array) - 2)
            newArr = np.array([DLinkedList() for i in range(dif)])
            self.array = np.concatenate((self.array, newArr))
        
        self.array[distList[node] + 1].insertAtTail(DLinkedListNode(node, None, None))
        self.size += 1
        return


    def getNext(self, graph, distList):
        for i in range(1, len(self.array)):
            if self.array[i].head is not None:
                self.size -= 1
                toReturn = self.array[i].popHead()
                return toReturn.val

    def update(self, node, alt, distList, prev):
        if prev == math.inf:
            listWNode = self.array[0]
            n = listWNode.popN(node)
            self.add(n.val, distList)
            return
        listWNode = self.array[int(prev) + 1]
        n = listWNode.popN(node)
        self.add(n.val, distList)
        return

    
class PriorityQueue:

    def __init__(self):
        self.pqueue = []
        #self.pqueue = np.array([],dtype=object)
        self.size = 0

    def __str__(self):
        return str(self.pqueue)

    def size(self):
        return self.size
    
    def name(self):
        return 'Priority Queue'
    
    def reset(self):
        self.pqueue = []
        #self.pqueue = np.array([[0, 0]],dtype=object)
        self.size = 0

    def add(self, node, distList):
        self.pqueue.append([node, distList[node]])
        #self.pqueue = np.append(self.pqueue, [int(node), distList[node]], axis=0)
        #if self.pqueue[0] == []:
            #self.pqueue = np.delete(self.pqueue, 0)
        self.size += 1
        return
    
    def getNext(self, graph, distList):
        #print(self.pqueue)
        min = math.inf
        toReturn = self.pqueue[0]
        for n in self.pqueue:
            if n[1] < min:
                min = n[1]
                toReturn = n

        self.pqueue.remove(toReturn)
        #self.pqueue = np.delete(self.pqueue, np.where(toReturn), axis=0)
        self.size -= 1
        return toReturn[0]
    
    def update(self, node, alt, distList, prev):
        for n in self.pqueue:
            if n[0] == node:
                n[1] = alt
                return

