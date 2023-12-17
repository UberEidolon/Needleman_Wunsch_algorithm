from random import randrange, random


# This class generates 2 similar sequences with some mutant differences for the basic algorithm

class Rand_seqs_pair:
	def __init__(self, length: int = 16, repl_chance: float = 0.05, ins_chance: float = 0.05, del_chance: float = 0.05) -> None:
		self.length = length
		self.letters = 'ACTG'
		self.repl_chance = repl_chance
		self.ins_chance = ins_chance
		self.del_chance = del_chance

		# We define chances of replacement, inseriton and deletion mutations in class arguments. Default is 0.05

	def __str__(self) -> str:
		return ''.join(str(''.join(j for j in i) + '\n') for i in self.generate_seqs_pair())

	def generate_seqs_pair(self) -> tuple:
		def rand_letter():
			return str((self.letters[randrange(4)]))
		
		seq1 = list(rand_letter() for i in range(self.length))
		seq2 = list(i for i in seq1)
		for n, i in enumerate(seq2):
			if random() <= self.repl_chance:
				seq2[n] = rand_letter()

			if random() <= self.ins_chance:
				seq2[n] = (rand_letter() + i)

			if random() <= self.del_chance:
				seq2[n] = ''

		return (''.join(i for i in seq1), ''.join(i for i in seq2))
	

if __name__ == "__main__":
	pair = Rand_seqs_pair()
	print(pair)