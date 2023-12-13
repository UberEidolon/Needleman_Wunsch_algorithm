from random import randrange, random


class Rand_seqs_pair:
    def __init__(self, length: int) -> None:
        self.length = length
        self.letters = 'ACTG'

    def generate(self) -> tuple:
        rand_letter = str((self.letters[randrange(4)]))
        seq1: str = str(rand_letter for i in range(self.length))
        seq2 = seq1
        del_chance = True if random() <= 0.05 else False
        ins_chance = True if random() <= 0.05 else False
        seq2 = (
            (
                seq2[n].replace(i, rand_letter) if (random() <= 0.05) else None
             ) for n, i in enumerate(seq2)
            )


        return (seq1, seq2)