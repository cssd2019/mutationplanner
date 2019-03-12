import string
from Bio import SeqIO, Seq

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

def string_case_converter( seq_dict ):
	
	for k, v in seq_dict.items():
		
		seq_dict[k] = v.lower()

	return seq_dict

def test_read_convert ( data ):
    fastaFile = fasta_to_dic(data)
    fastaFileConverted = string_case_converter(fastaFile)
    print(fastaFileConverted)


test_read_convert("test.fasta")
