class MyStack:
    def __init__(self):
        self.elements = []

    def push(self, obj):
        self.elements.append(obj)

    def pop(self):
        if len(self.elements) == 0:
            return None
        result = self.elements[-1]
        self.elements = self.elements[:-1]
        return result

    def peek(self):
        return self.elements[-1] if len(self.elements) > 0 else None

    def is_empty(self):
        return len(self.elements) == 0
