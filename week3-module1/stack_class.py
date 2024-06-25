class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def pop(self):
        if self.is_empty():
            raise IndexError("Underflow")
        return self.stack.pop()

    def push(self, value):
        if self.is_full():
            raise IndexError("Overflow")
        return self.stack.append(value)

    def top(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.stack[-1]


stack1 = MyStack(5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
