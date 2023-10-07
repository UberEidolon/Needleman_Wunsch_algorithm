from pandas import DataFrame
import numpy


# Pandas DataFrame table is using for view algorithm's matrix
# Numpy is using for work with matrix data

class Matrix:
    def __init__(self, seq1: str, seq2: str, match: int, dismatch:int, insertion: int) -> None:
        self.seq1 = ' ' + seq1
        self.seq2 = ' ' + seq2
        self.match = match
        self.dismatch = dismatch
        self.insertion = insertion
        self.matrix = numpy.zeros(
            shape=(len(self.seq1), len(self.seq2)), dtype="int"
            )

    def __str__(self):
        return str(DataFrame(
            data=self.matrix,
            index=list(self.seq1),
            columns=list(self.seq2)
            ))

    def algorithm(self):
        def first_fill():
            for i in range(1, len(self.seq2)):
                self.matrix[0, i] = self.matrix[0, i-1] + self.insertion

            for i in range(1, len(self.seq1)):
                self.matrix[i, 0] = self.matrix[i-1, 0] + self.insertion

        def body():
            for i in range(
                (len(self.seq1) - 1 ) * (len(self.seq2) - 1)
                ):
                x, y = 1, 1
                up = self.matrix[x, y+1] + self.insertion
                left = self.matrix[x+1, y] + self.insertion
                dgnl = self.matrix[x, y] + (self.match if self.seq1[y+1] == self.seq2[x+1] else self.dismatch)

                self.matrix[x+1, y+1] = max(up, left, dgnl)
                x += 1
                y += 1
                print(self)

        return first_fill(), body()

table = Matrix(seq1="ACTG", seq2="ACG", match=2, dismatch=-1, insertion=-2)
table.algorithm()

print(table)


# Алгоритм почти готов, надо нормально настроить индексы x и y
