from random import randrange, random


# This class generates 2 similar sequences with some mutant differences for the basic algorithm

class Rand_seqs_pair:
	def __init__(self, length: int = 64, repl_chance: float = 0.05, ins_chance: float = 0.05, del_chance: float = 0.05) -> None:
		self.length = length
		self.letters = 'ACTG'
		self.repl_chance = repl_chance
		self.ins_chance = ins_chance
		self.del_chance = del_chance

		# We define chances of replacement, insertion and deletion mutations in class arguments. Default is 0.05

	def generate_seqs_pair(self) -> tuple:
		def rand_letter():
			return str((self.letters[randrange(4)]))
		
		seq1: list = list(rand_letter() for i in range(self.length))
		seq2 = list(i for i in seq1)
		for n, i in enumerate(seq2):
			if random() <= self.repl_chance:
				seq2[n] = rand_letter()

			if random() <= self.ins_chance:
				seq2[n] = (rand_letter() + i)

			if random() <= self.del_chance:
				seq2[n] = ''


		return (seq1, seq2)
	

# pair = Rand_seqs_pair().generate_seqs_pair()
# print(''.join(i for i in pair[0]), ''.join(i for i in pair[1]), sep='\n')
