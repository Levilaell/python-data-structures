class Node: # type: ignore
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def __repr__(self):
        items = []

        curr = self.front

        while curr is not None:
            items.append(str(curr))
            curr = curr.next

        return ' <- '.join(items) if items else 'Empty'

    def enqueue(self, value):
        new_node = Node(value)
        
        if self.rear is None:
            self.rear = self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def dequeue(self):
        if self.front is None: 
            return None
        
        val = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1  

        return val

    def peek(self):
        if self.front is None:
            return None

        return self.front.value

    def is_empty(self):
        return self.front is None

