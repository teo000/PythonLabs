class MyQueue:
    def __init__(self):
        self.__elements = []

    def push(self, obj):
        self.__elements.append(obj)

    def pop(self):
        if len(self.__elements) == 0:
            return None
        result = self.__elements[0]
        self.__elements = self.__elements[1:]
        return result

    def peek(self):
        return self.__elements[0] if len(self.__elements) > 0 else None

    def is_empty(self):
        return len(self.__elements) == 0

    def len(self):
        return len(self.__elements)