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
            row, column = 1, 1
            for i in self.matrix[1:, 1:]:
                for j in i:
                    print(row, column, sep=":")
                    print(table)
                    up = self.matrix[row, column-1]
                    left = self.matrix[row-1, column]
                    dgnl = self.matrix[row-1, column-1]
                    print(f'max is: {max(dgnl, left, up)}')
                    if dgnl == max(dgnl, up, left):
                        if self.seq1[row] == self.seq2[column]:
                            self.matrix[row, column] = dgnl + self.match
                        else:
                            self.matrix[row, column] = dgnl + self.dismatch
                    elif left == max(dgnl, up, left):
                        self.matrix[row, column] = self.matrix[row-1, column] + self.insertion
                    elif up == max(dgnl, up, left):
                        self.matrix[row, column] = self.matrix[row, column-1] + self.insertion

                    column += 1
                    print(table, '\n', '-------------')
                    
                
                row += 1
                column = 1



        return first_fill(), body()


table = Matrix(seq1="ACTG", seq2="ACG", match=2, dismatch=-1, insertion=-2)
table.algorithm()