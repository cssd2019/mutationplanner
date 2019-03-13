import read_fasta as rf
import convert_fasta_case as cfc
import create_pi_dict as cpd
import combine_pi_scores as cps
import make_trace_data as mtd
import make_plot as mp

def mutation_analyser(octamers_file_path, fasta_file_path, fasta_record_id):
    # 1. Read fasta file
    fasta_dict = rf.read_fasta(fasta_file_path)
    print(fasta_dict)

    # 2. Convert fasta sequence case to all lower
    fasta_dict = cfc.convert_fasta_case(fasta_dict)
    print(fasta_dict)

    # 3. Create P and I dictionary from octamers text file
    pi_dict = cpd.create_pi_dict(octamers_file_path)
    print(pi_dict)

    # 4. Combine P and I score into a single score
    pi_dict = cps.combine_pi_score(pi_dict, 3)

    # 5. Make the make/initial trace for display
    fasta_seq = fasta_dict[fasta_record_id]
    x_data, y_data = mtd.make_trace_data(fasta_seq, pi_dict)

    # 6. Call the plot function
    mp.make_plot(x_data, y_data, fasta_seq, pi_dict)


if __name__ == '__main__':
    octamers_file_path = "./data/octamers.txt"
    fasta_file_path = "./data/test.fasta"
    fasta_record_id = 'wt'
    mutation_analyser(octamers_file_path, fasta_file_path, fasta_record_id)