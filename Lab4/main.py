from Matrix import Matrix
from MyQueue import MyQueue
from MyStack import MyStack

s = MyStack()
# s = MyQueue()
s.push(5)
s.push("test")

print(s.is_empty())

print(s.pop())
print(s.peek())
print(s.pop())

print(s.is_empty())


m = Matrix(3, 5)

print(m.elements)

m.set(2, 3, 5)
m.set(1, 2, 7)
m.get(1, 2)

m.print()
m_transposed = m.transpose()
m_transposed.print()

m1 = Matrix(1, 2, init=3)
m2 = Matrix(2, 2, init=2)
m2.set(1, 0, 5)
m1.print()
m2.print()
m1.multiply(m2).print()

m2.apply_on_each(lambda a: a*a)
m2.print()
