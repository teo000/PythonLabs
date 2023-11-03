class Matrix:
    def __init__(self, n, m, init=0):
        self.n = n
        self.m = m
        self.elements = [[init for _ in range(m)] for _ in range(n)]

    def get(self, i, j):
        return self.elements[i][j]

    def set(self, i, j, value):
        self.elements[i][j] = value

    def transpose(self):
        new_matrix = Matrix(self.m, self.n)
        for j in range(self.m):
            for i in range(self.n):
                new_matrix.set(j, i, self.elements[i][j])
        return new_matrix

    def multiply(self, other_matrix):
        if self.m != other_matrix.n:
            return None

        new_matrix = Matrix(self.n, other_matrix.m)
        for row in range(self.n):
            for col in range(other_matrix.m):
                value = 0
                for k in range(self.m):
                    value += self.get(row, k) * other_matrix.get(k, col)
                new_matrix.set(row, col, value)

        return new_matrix

    def apply_on_each(self, fct):
        for i in range(self.n):
            for j in range(self.m):
                self.elements[i][j] = fct(self.elements[i][j])

    def print(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.elements[i][j], end=" ")
            print()
        print()
