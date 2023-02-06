class Stack:
    def __init__(self) :
        self.items = []

    def push(self , item):
        self.items.append(item)

    def is_empty(self):
        return not self.items

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

if __name__=="__main__":
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(1)
    s.push(3)
    s.push(5)
    s.push(7)
    print(s)
    print(s.size())
    print(s.pop())
    print(s)
    print(s.size())