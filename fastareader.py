from Bio import SeqIO, Seq

"""
makes a dictionary (seq_dict) with the ids as keys and 

"""


#seq_dict = SeqIO.to_dict(SeqIO.parse("test.fasta", "fasta"))
#print(seq_dict)
#print("######################")

def fasta_to_dic(filename):
	seq_dict = {}
	for sequence in SeqIO.parse(filename, "fasta"):#
		#test.fasta: 
		#print(sequence.id)
		s = sequence.seq
		#print(repr(s))
		s = str(sequence.seq)
		#obtaining a sequence string from a .seq object is done with str()
		#print(s)
		#print(len(sequence))
		seq_dict[sequence.id] = s

	return seq_dict

a = fasta_to_dic("test.fasta")

print(a)
