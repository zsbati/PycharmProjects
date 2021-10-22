class Stack:

    def __init__(self):
        self.content = []

    def push(self, el):
        self.content.append(el)

    def pop(self):
        return self.content.pop()

    def peek(self):
        return self.content[-1]

    def is_empty(self):
        if len(self.content) == 0:
            return True
        return False


