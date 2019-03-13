import make_main_trace_data as mmtd
import create_pi_dict as cpd
import matplotlib.pyplot as plt
import numpy as np
from make_plot import make_plot 
import string
from Bio import SeqIO, Seq
from fastareader import fasta_to_dic
from reader_converter import fastadic_lower


octamers_file_path = "./data/octamers.txt"
# Read the PI dictionary
pi_dict = cpd.create_pi_dict(octamers_file_path)


fastadic = fasta_to_dic( "test.fasta" )
fastadic_lower = fastadic_lower(fastadic)
fasta_seq =  fastadic_lower["wt"]
#for k, v in fastadic_lower.items():
#    print(k,v)
 #   if k == "wt":
 #       fasta_seq = v

#        break

print("#####", fasta_seq)
#fasta_seq is need by make_plot
    
x_data, y_data = mmtd.make_main_trace_data(fasta_seq, pi_dict)

make_plot(x_data, y_data, fasta_seq)

