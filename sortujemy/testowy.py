class kopiec:
    def __init__(self, items = []):
        super().__init__()
        self.heap = []
        for i in items:
            self.heap.append(i)
            #self._siftdown(0, len(self.heap) - 1)
            self.__floatUp(len(self.heap) - 1)

    def heappush(self, item):
        """Push item onto heap, maintaining the heap invariant."""
        self.heap.append(item)
        self._siftdown(0, len(self.heap)-1)
        #self.__floatUp(len(self.heap) - 1)

    def heappop(self):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        lastelt = self.heap.pop()    # raises appropriate IndexError if heap is empty
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = lastelt
            self._siftup(0)
        else:
            returnitem = lastelt
        return returnitem

    def heapify(x):
        """Transform list into a heap, in-place, in O(len(x)) time."""
        n = len(x)
        for i in reversed(xrange(n//2)):
            self._siftup(x, i)

    def _siftdown(self, startpos, pos):
        newitem = self.heap[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self.heap[parentpos]
            #if cmp_lt(newitem, parent):
            if newitem < parent:
                self.heap[pos] = parent
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _siftup(self, pos):
        endpos = len(self.heap)
        startpos = pos
        newitem = self.heap[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not self.heap[childpos] < self.heap[rightpos]:
                childpos = rightpos
                # Move the smaller child up.
                self.heap[pos] = self.heap[childpos]
                pos = childpos
                childpos = 2*pos + 1
                # The leaf at pos is empty now.  Put newitem there, and bubble it up
                # to its final resting place (by sifting its parents down).
        self.heap[pos] = newitem
        self._siftdown(startpos, pos)


# Simple sanity test
#heap = []
#data = [13, 85, 1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
#for item in data:
#    heappush(heap, item)
#    sort = []
#    while heap:
#        sort.append(heappop(heap))
#print (sort)

m = kopiec([0, 13, 5, 95, 3, 21])
print (m.heap)
#for i in m.heap:
#    m.heappush(i)
while m.heap:
    print (m.heappop())

