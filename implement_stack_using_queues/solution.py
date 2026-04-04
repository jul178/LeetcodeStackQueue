class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    def pop(self):
        if self.is_empty():
            return None
        val = self.head.val
        self.head = self.head.next
        return val


    def peek(self):
        return self.head.val if self.head else None

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        probe = self.head
        while probe is not None:
            count += 1
            probe = probe.next
        return count

class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        size = self.queue.size()
        self.queue.add(x)
        for _ in range(size):
            self.queue.add(self.queue.pop())


    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.is_empty()
