class Matrix:
    def __init__(self, n, m, init=0):
        self.__n = n
        self.__m = m
        self.__elements = [[init for _ in range(m)] for _ in range(n)]

    def get(self, i, j):
        return self.__elements[i][j]

    def get_n(self):
        return self.__n

    def get_m(self):
        return self.__m

    def set(self, i, j, value):
        self.__elements[i][j] = value

    def transpose(self):
        new_matrix = Matrix(self.__m, self.__n)
        for j in range(self.__m):
            for i in range(self.__n):
                new_matrix.set(j, i, self.__elements[i][j])
        return new_matrix

    def multiply(self, other_matrix):
        if self.__m != other_matrix.get_n():
            return None

        new_matrix = Matrix(self.__n, other_matrix.get_m())
        for row in range(self.__n):
            for col in range(other_matrix.get_m()):
                value = 0
                for k in range(self.__m):
                    value += self.get(row, k) * other_matrix.get(k, col)
                new_matrix.set(row, col, value)

        return new_matrix

    def apply_on_each(self, fct):
        for i in range(self.__n):
            for j in range(self.__m):
                self.__elements[i][j] = fct(self.__elements[i][j])

    def print(self):
        for i in range(self.__n):
            for j in range(self.__m):
                print(self.__elements[i][j], end=" ")
            print()
        print()
