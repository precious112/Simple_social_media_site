from .Linkedlist import LinkedList
class queue:
	def __init__(self):
		self.items=LinkedList()
		self.frontIdx=0
	def dequeue(self):
		if self.isEmpty():
			raise RuntimeError("Attempt to dequeue an empty queue")
		
		item=self.items[self.frontIdx]
		del self.items[self.frontIdx]
		return item
	def enqueue(self,item):
		self.items.append(item)
	def front(self):
		if self.isEmpty():
			raise RuntimeError("Attempt to dequeue an empty queue")
		return self.items[self.frontIdx]
	def isEmpty(self):
		return self.frontIdx==len(self.items)
	def clear(self):
		self.items=LinkedList()
		self.frontIdx=0
def main():
    q = queue()
    items = list(range(10))
    items2 = []
    
    for k in items:
        q.enqueue(k)
        
    if q.front() == 0:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")
        
    while not q.isEmpty():
        items2.append(q.dequeue())
        
    if items2 != items:
        print("Test 2 Failed")
    else:
        print("Test 2 Passed")
    q.clear()

    for k in items:
        q.enqueue(k)   
      
    items2 = []
    
    while not q.isEmpty():
        items2.append(q.dequeue())  
        
    if items2 != items:
        print("Test 3 Failed")
    else:
        print("Test 3 Passed")
    
    try:
        q.dequeue()
        print("Test 4 Failed")
        
    except RuntimeError:
        print("Test 4 Passed")
    except:
        print("Test 4 Failed")

    try:
        q.front()
        print("Test 5 Failed")
        
    except RuntimeError:
        print("Test 5 Passed")
    except:
        print("Test 5 Failed")  
        
if __name__=="__main__":
    main()
			