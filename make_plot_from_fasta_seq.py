import create_pi_dict as cpd
import matplotlib.pyplot as plt

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


fastadic = fasta_to_dic("test.fasta")
fastadic_lower = string_case_converter(fastadic)
for k, v in fastadic_lower.items():
    print(k,v)
    if k == "wt":
        fasta_seq = v
        break
#for k, v in n.items():
#    print(k,v)

def make_plot(pi_dict):

    # Read fasta file
    #fasta_seq = "ttagGATAGAAGATATTGAACATTTTTGTATTTGGTGGGGAGAGAGCTCAGAGGGAGGAAGAAATAGAAGATGCAGAAGAGGATGGACTAATTGATGGAGCAGAGTCTTTGAGgttaa"
    #fasta_seq = fasta_seq.lower()

    # Merged-scripts

    # make main trace data
    kmer_length = 8
    fasta_length = len(fasta_seq)
    y_data = [0, 0, 0, 0]
    x_data = [x for x in range(fasta_length)]
    for idx, nt in enumerate(fasta_seq):
        if idx > (fasta_length - kmer_length):
            break
        start_idx = idx
        end_idx = start_idx + kmer_length
        current_octamer = fasta_seq[start_idx:end_idx]
        octamer_data = sum(pi_dict[current_octamer])
        y_data.append(octamer_data)
        print(idx, current_octamer, octamer_data)
    y_data.append(0)
    y_data.append(0)
    y_data.append(0)
    #
    # print(x_data)
    # print(y_data)
    #
    #
    # print(len(x_data), len(y_data))
    # print(dict(zip(x_data, y_data)))

    plt.plot(x_data, y_data, '-', linewidth=2, markersize=12)
    plt.show()
    # Compute combined PI score

if __name__ == "__main__":
    octamers_file_path = "./data/octamers.txt"
    # Read the PI dictionary
    pi_dict = cpd.create_pi_dict(octamers_file_path)

    make_plot(pi_dict)