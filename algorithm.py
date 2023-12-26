from pandas import DataFrame
import numpy
from mutant_generator import Rand_seqs_pair


class Matrix:
    def __init__(self, match: int, dismatch:int, insertion: int, seqs: tuple) -> None:
        self.seqs: tuple = tuple(list(' ' + _) for _ in seqs)
        self.match = match
        self.dismatch = dismatch if dismatch <= 0 else dismatch * -1
        self.insertion = insertion if insertion <= 0 else insertion * -1
        self.matrix = numpy.zeros(
            shape=(tuple(len(_) for _ in self.seqs)),
            dtype="int"
        )

    def __str__(self) -> str:
        pair = self.level_out()
        return f'{pair[0]}\n{pair[1]}'

    def create_table(self) -> str:
        return str(DataFrame(
            data=self.matrix,
            index=list(self.seqs[0]),
            columns=list(self.seqs[1])
            ))

    def algotithm(self):
        def head_fill():
            for i in range(1, len(self.seqs[1])):
                self.matrix[0, i] = self.matrix[0, i-1] + self.insertion

            for i in range(1, len(self.seqs[0])):
                self.matrix[i, 0] = self.matrix[i-1, 0] + self.insertion

        def body_fill():
            row = column = 1
            seq_1 = self.seqs[0]
            seq_2 = self.seqs[1]
            for i in self.matrix[1:, 1:]:
                for _ in i:
                    up: int = self.matrix[row-1, column]
                    left: int = self.matrix[row, column-1]
                    dgnl: int = self.matrix[row-1, column-1]

                    self.matrix[row, column] = max(
                        up + self.insertion,
                        left + self.insertion,
                        dgnl + (
                        self.match if seq_1[row] == seq_2[column] else self.dismatch
                        )
                    )

                    column += 1
                
                row += 1
                column = 1
        
        head_fill()
        body_fill()
        return self.create_table()

    def level_out(self):
        self.algotithm()
        first_str = second_str = ''
        i = len(self.matrix) - 1
        j = len(self.matrix[0]) - 1
        while (i and j) != 0:
            up = self.matrix[i][j-1]
            left = self.matrix[i-1][j]
            dngl = self.matrix[i-1][j-1]
            if max(up, left, dngl) == up:
                first_str += '-'
                second_str += self.seqs[1][j]
                j += -1

            elif max(up, left, dngl) == left:
                first_str += self.seqs[0][i]
                second_str += '-'
                i += -1

            else:
                first_str += self.seqs[0][i]
                second_str += self.seqs[1][j]
                i += -1
                j += -1

        first_str = list(reversed(first_str))
        second_str = list(reversed(second_str))
        for n, i in enumerate(first_str):
            if i == '-':
                first_str[n], first_str[n-1] = first_str[n-1], '-'

        for n, i in enumerate(second_str):
            if i == '-':
                second_str[n] = second_str[n-1]
                second_str[n-1] = '-'
        pair = []
        pair.append(''.join(i for i in first_str))
        pair.append(''.join(i for i in second_str))
        return pair

if __name__ == "__main__":
    random_table = Matrix(
        seqs=Rand_seqs_pair().generate_seqs_pair(),
        match=2,
        dismatch=-1,
        insertion=-2
        )
    
    determined_table = Matrix(
        seqs=('ATCACAG',
              'TGCAGTAG'),
        match=2,
        dismatch=-1,
        insertion=-2
        )
    
    print(random_table.algotithm())
    print(random_table)
    