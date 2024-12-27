from operator import truediv
import AllQueueDS
import math
import fibHeap
import fibHeapV2
import numpy as np

class BinaryHeap:

    def __init__(self):
        self.heap = []
        #self.heap = np.array([])
        self.size = 0

    def __str__(self):
        return str(self.heap)
    
    def name(self):
        return 'Binary Heap'
    
    def reset(self):
        self.heap = []
        self.size = 0
    
    def add(self, node, distList):
        self.heap.append([node, distList[node]])
        #np.append(self.heap, [node, distList[node]], axis=0)
        self.size += 1

        if self.size == 1:
            return
        
        n = int((len(self.heap)//2)-1)
        for i in range(n, -1, -1):
            self.heapify(self.heap,i)

        return
        


    def getNext(self, graph, distList):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]

        toReturn = self.heap.pop()

        n = int((len(self.heap)//2)-1)
        for i in range(n, -1, -1):
            self.heapify(self.heap,i)

        self.size -= 1

        return toReturn[0]

    def update(self, node, alt, distList, prev):
        count = 0
        for n in self.heap:
            if n[0] == node:
                self.heap[count][1] = alt
                n = int((len(self.heap)//2)-1)
                for i in range(n, -1, -1):
                    self.heapify(self.heap,i)
                return
            count += 1
    
    def heapify(self, heap, root):
        left = 2 * root + 1
        right = 2 * root + 2

        if left < len(heap) and heap[left][1] < heap[root][1]:
            smallest = left
        else:
            smallest = root
        if right < len(heap) and heap[right][1] < heap[smallest][1]:
            smallest = right
        if smallest != root:
            heap[root], heap[smallest] = heap[smallest], heap[root]
            self.heapify(heap, smallest)
    


class FibonacciHeap:
    def __init__(self):
        self.heap = fibHeapV2.FibonacciHeap()
        self.size = 0
        self.nodes = []
        
    def name(self):
        return 'Fibonacci Heap'
    
    def reset(self):
        self.heap = fibHeapV2.FibonacciHeap()
        self.size = 0
        self.nodes = []

    def add(self, node, distList):
        n = self.heap.insert(distList[node], node)
        self.nodes.append(n)
        self.size += 1
        return
    
    def getNext(self, graph, distList):
        toReturn = self.heap.extract_min()
        self.size -= 1
        return toReturn.value
    
    def update(self, node, alt, distList, prev):
        for n in self.nodes:
            if n.value == node:
                self.heap.decrease_key(n, alt)
                return
    


class TwoThreeHeap:
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        return str(self.root)

    def name(self):
        return 'Two-Three Heap'
    
    def reset(self):
        self.root = None
        self.size = 0
        
    def add(self, node, distList):
        self.insert(self.root, (node, distList[node]))
        self.size += 1
        return
        
    def insert(self, candidate, key):
        if self.root is None:
            self.root = TwoThreeNode(key)
            return
        
        if candidate.isLeaf():
            isOverflow = candidate.addKey(key)
            if isOverflow:
                #print(repr(candidate))
                self.fixOverflow(candidate)
        else:
            if candidate.key1[1] > key[1]:
                self.insert(candidate.left, key)
            elif candidate.key1[1] <= key[1] and candidate.is2Node():
                self.insert(candidate.center, key)
            else:
                if candidate.key2[1] > key[1]:
                    self.insert(candidate.center, key)
                else:
                    self.insert(candidate.right, key)

    def fixOverflow(self, overflowNode):
        node = overflowNode

        #print(str(self))
        #print(repr(node))

        while node.isFull():
            if node == self.root:
                newRoot = TwoThreeNode(node.key2)
                self.root = newRoot
                newRootLeft = TwoThreeNode(node.key1)
                newRootRight = TwoThreeNode(node.key3)
                newRoot.left = newRootLeft
                newRoot.center = newRootRight
                newRootLeft.parent = newRoot
                newRootRight.parent = newRoot
                if not node.isLeaf():
                    newRootLeft.left = node.left
                    newRootLeft.center = node.center
                    newRootRight.left = node.center2
                    newRootRight.center = node.right
                    
                    newRootLeft.left.parent = newRootLeft
                    newRootLeft.center.parent = newRootLeft
                    newRootRight.left.parent = newRootRight
                    newRootRight.center.parent = newRootRight
                return
            else:
                node.parent.addKey(node.key2)
                newLeft = TwoThreeNode(node.key1)
                newRight = TwoThreeNode(node.key3)

                if not node.isLeaf():
                    newLeft.left = node.left
                    newLeft.left.parent = newLeft

                    newLeft.center = node.center
                    newLeft.center.parent = newLeft

                    newRight.left = node.center2
                    newRight.left.parent = newRight

                    newRight.center = node.right
                    newRight.center.parent = newRight

                newLeft.parent = node.parent
                newRight.parent = node.parent

                if node.parent.isFull():
                    if node.parent.left == node:
                        node.parent.left = newLeft
                        node.parent.center2 = node.parent.center
                        node.parent.center = newRight

                    elif node.parent.center == node:
                        node.parent.center = newLeft
                        node.parent.center2 = newRight

                    else:
                        node.parent.center2 = newLeft
                        node.parent.right = newRight

                else:
                    if node.parent.left == node:
                        node.parent.left = newLeft
                        node.parent.right = node.parent.center
                        node.parent.center = newRight
                    else:
                        node.parent.center = newLeft
                        node.parent.right = newRight
                
                if node.parent.parent is None:
                    self.root = node.parent

            node = node.parent
            


    def getNext(self, graph, distList):
        print('getnext')
        print(self.root)
        runner = self.root
        while runner.left is not None:
            runner = runner.left
        
        toReturn = runner.key1[0]

        print(repr(runner.key1))
        
        self.removeV2(runner, runner.key1)
        self.size -= 1
        
        print('after')
        print(self.root)
        return toReturn
    
    def find(self, head, key):
        if head.contains(key):
            return head
        
        if head.key1[1] > key[1]:
                self.find(head.left, key)
        elif head.key1[1] <= key[1] and head.is2Node():
                self.find(head.center, key)
        else:
            if head.key2[1] > key[1]:
                self.find(head.center, key)
            else:
                self.find(head.right, key)
    
    def findINF(self, head, key):
        if head.contains(key):
            #print('found: ' + str(head))
            return head
        
        if head.left is not None:
            self.findINF(head.left, key)
        if head.center is not None:
            self.findINF(head.center, key)
        if head.right is not None:
            self.findINF(head.right, key)
    
    def removeV2(self, node, key):
        if node.isLeaf():
            node.removeKey(key)
        else:
            if key == node.key1:
                swap = node.left.getMax()
                node.removeKey(node.key1)
                node.key1 = swap
                self.removeV2(node.left, swap)
            else:
                if node.is2Node:
                    swap = node.center.key1
                    rem = node.center
                else:
                    swap = node.right.key1
                    rem = node.right

                node.removeKey(node.key2)
                node.key2 = swap
                self.removeV2(rem, swap)
        print('pre-fix')
        print(self.root)

        self.fixUnderflow(node)
    
    #CURRENT ERROR: removing when all keys/most keys are inf
    def remove(self, candidate, key):
        print("c: " + repr(candidate))
        print("k: " + str(key))
        if candidate.contains(key):
            if candidate.isLeaf():
                candidate.removeKey(key)
            else:
                if key == candidate.key1:
                    swap = candidate.left.getMax()
                    candidate.removeKey(candidate.key1)
                    candidate.key1 = swap
                    self.remove(candidate.left, swap)
                else:
                    if candidate.is2Node:
                        swap = candidate.center.key1
                        rem = candidate.center
                    else:
                        swap = candidate.right.key1
                        rem = candidate.right

                    candidate.removeKey(candidate.key2)
                    candidate.key2 = swap
                    self.remove(rem, swap)
        else:
            if candidate.key1[1] > key[1]:
                self.remove(candidate.left, key)
            elif candidate.key1[1] <= key[1] and candidate.is2Node():
                self.remove(candidate.center, key)
            else:
                if candidate.key2[1] > key[1]:
                    self.remove(candidate.center, key)
                else:
                    self.remove(candidate.right, key)
        
        #print(str(self))
        self.fixUnderflow(candidate)


    def fixUnderflow(self, node):
        while node.isUndersized():
            if node.parent is None:
                self.root = node.left
            elif node.getOpenSibling() is None:
                if node.parent.is2Node():
                    if node.parent.left == node:
                        node.key1 = node.parent.key1
                        node.parent.key1 = node.parent.center.key1
                        node.parent.center.key1 = node.parent.center.key2
                        node.parent.center.key2 = None
                        
                        if not node.isLeaf():
                            node.center = node.parent.left
                            node.center.parent = node

                            node.parent.center.left = node.parent.center.center
                            node.parent.center.center = node.parent.center.right
                            node.parent.center.right = None

                    else:
                        node.key1 = node.parent.key1
                        node.parent.key1 = node.parent.left.key2
                        node.parent.left.key2 = None

                        if not node.isLeaf():
                            node.center = node.left
                            node.left = node.parent.left.right
                            node.left.parent = node

                            node.parent.left.right = None
                else:
                    if node.parent.left == node:
                        node.key1 = node.parent.key1
                        node.parent.key1 = node.parent.center.key1
                        node.parent.center.key1 = node.parent.center.key2
                        node.parent.center.key2 = None

                        if not node.isLeaf():
                            node.center = node.parent.center.left
                            node.center.parent = node

                            node.parent.center.left = node.parent.center.center
                            node.parent.center.center = node.parent.center.right
                            node.parent.center.right = None

                    elif node.parent.center == node:
                        node.key1 = node.parent.key2
                        node.parent.key2 = node.parent.right.key1
                        node.parent.right.key1 = node.parent.right.key2
                        node.parent.right.key2 = None

                        if not node.isLeaf():
                            node.center = node.parent.right.left
                            node.center.parent = node

                            node.parent.right.left = node.parent.right.center
                            node.parent.right.center = node.parent.right.right
                            node.parent.right.right = None
                    else:
                        node.key1 = node.parent.key2
                        node.parent.key2 = node.parent.center.key2
                        node.parent.center.key2 = None

                        if not node.isLeaf():
                            node.center = node.left
                            node.left = node.parent.center.right
                            node.left.parent = node

                            node.parent.center.right = None
            else:                
                if node.parent.is2Node():
                    if node.parent.left == node:
                        node.key1 = node.parent.key1
                        node.parent.key1 = None
                        #node.key2 = node.parent.center.key1

                        if not node.isLeaf():
                            node.center = node.parent.center.left
                            node.center.parent = node

                            node.right = node.parent.center.center
                            node.right.parent = node

                        node.parent.center = None
                    else:
                        node.key1 = node.parent.key1
                        node.parent.key1 = None
                        node.parent.left.key2 = node.key1
                        node.parent.center = None   

                        if not node.isLeaf():
                            node.parent.left.right = node.left
                            node.parent.left.right.parent = node.parent.left.right
                else:
                    if node.parent.left == node:
                        node.key1 = node.parent.key1
                        node.parent.key1 = node.parent.key2
                        node.parent.key2 = None
                        node.key2 = node.parent.center.key1

                        if not node.isLeaf():
                            node.center = node.parent.center.left
                            node.center.parent = node

                            node.right = node.parent.center.center
                            node.right.parent = node
                        node.parent.center = node.parent.right
                        node.parent.right = None
                    elif node.parent.center == node:
                        if node.parent.right.key2 is None:
                            node.key1 = node.parent.key2
                            node.parent.key2 = None
                            node.key2 = node.parent.right.key1

                            if not node.isLeaf():
                                node.center = node.parent.right.left
                                node.center.parent = node

                                node.right = node.parent.right.center
                                node.right.parent = node

                            node.parent.right = None
                        else:
                              node.key1 = node.parent.key1
                              node.parent.key1 = node.parent.key2
                              node.parent.key2 = None
                              node.parent.left.key2 = node.key1
                              node.parent.center = node.parent.right
                              node.parent.right = None

                              if not node.isLeaf():
                                  node.parent.left.right = node.left
                                  node.parent.left.right.parent = node.parent.left.right
                    else:
                        node.key1 = node.parent.key2
                        node.parent.key2 = None
                        node.parent.center.key2 = node.key1
                        node.parent.right = None

                        if not node.isLeaf():
                            node.parent.center.right = node.left
                            node.parent.center.right.parent = node.parent.center.right
            

            node = node.parent
            if node is None:
                break

                    




    def update(self, node, alt, distList, prev):
        #print('up')
        #print(self.root)
        if prev is math.inf:
            #print('want: ' + str((node, prev)))
            toRemove = self.findINF(self.root, (node, prev))
        else:
            toRemove = self.find(self.root, (node, prev))
            
        
        self.removeV2(toRemove, (node, prev))

        newNode = TwoThreeNode((node, alt))
        self.insert(self.root, newNode)
        return

        

class TwoThreeNode:
    def __init__(self, key):
        self.key1 = key
        self.key2 = None
        self.key3 = None

        self.left = None
        self.center = None
        self.center2 = None
        self.right = None

        self.parent = None

    def __str__(self):
        return self.toPrint(0)
    
    def toPrint(self, level):
        toReturn = '\t' * level + repr(self) + '\n'
        if self.isLeaf():
            return toReturn
        toReturn += self.left.toPrint(level+1)
        toReturn += self.center.toPrint(level+1)
        if not self.is2Node():
            toReturn += self.right.toPrint(level+1)
        
        return toReturn
    
    def __repr__(self):
        toReturn = '(' + str(self.key1)

        if self.key2 is not None:
            toReturn += '|' + str(self.key2)

        if self.key3 is not None:
            toReturn += '|' + str(self.key3)
        
        toReturn += ')'

        return toReturn
        

    def isLeaf(self):
        if self.left is None and self.center is None and self.right is None:
            return True
        else:
            return False
        

    def contains(self, key):
        return self.key1 == key or self.key2 == key
    

    def getMax(self):
        if self.key2 is None:
            return self.key1
        else:
            return self.key2
    
    def getOpenSibling(self):
        #print(self.parent.center)
        if self.parent.left == self:
            if self.parent.center.key2 is None:
                return self.parent.center
            
        if self.parent.is2Node():
            if self.parent.left.key2 is None:
                return self.parent.left
        else:
            if self.parent.center == self:
                if self.parent.right.key2 is None:
                    return self.parent.right
                elif self.parent.left.key2 is None:
                    return self.parent.left
            else:
                if self.parent.center.key2 is None:
                    return self.parent.center
        
        return None


    def is2Node(self):
        return self.key2 is None
            

    def isFull(self):
        return self.key3 is not None
    
    def isUndersized(self):
        return self.key1 is None
    
        
    def addKey(self, newKey):
        if self.key2 is None:
            if self.key1[1] <= newKey[1]:
                self.key2 = newKey
                return False
            else:
                self.key2 = self.key1
                self.key1 = newKey
                return False
        else:
            if self.key2[1] <= newKey[1]:
                self.key3 = newKey
                return True
            elif self.key1[1] <= newKey[1]:
                self.key3 = self.key2
                self.key2 = newKey
                return True
            else:
                self.key3 = self.key2
                self.key2 = self.key1
                self.key1 = newKey
                return True
    

    def removeKey(self, key):
        if self.key1 == key:
            self.key1 = None
        elif self.key2 == key:
            self.key2 = None

