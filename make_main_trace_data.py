import numpy as np

def make_main_trace_data(fasta_seq, pi_dict):
    # Read fasta file
    fasta_seq = "ttagGATAGAAGATATTGAACATTTTTGTATTTGGTGGGGAGAGAGCTCAGAGGGAGGAAGAAATAGAAGATGCAGAAGAGGATGGACTAATTGATGGAGCAGAGTCTTTGAGgttaa"
    fasta_seq = fasta_seq.lower()

    # make main trace data
    kmer_length = 8
    fasta_length = len(fasta_seq)
    y_data = np.zeros(fasta_length + 1)
    y_data.fill(np.nan)
    x_data = np.arange(start=0, stop=fasta_length + 1, step=1, dtype='int')
    for idx, nt in enumerate(fasta_seq):
        if idx > (fasta_length - kmer_length):
            print('end', idx)
            break

        start_idx = idx
        end_idx = start_idx + kmer_length
        current_octamer = fasta_seq[start_idx:end_idx]

        # call maria's function here
        octamer_data = sum(pi_dict[current_octamer])
        ####

        y_idx = int(idx + (kmer_length / 2))
        y_data[y_idx] = octamer_data
        print(idx, current_octamer, octamer_data)

    return x_data, y_data


if __name__ == "__main__":
    import create_pi_dict as cpd
    octamers_file_path = "./data/octamers.txt"
    fasta_seq = "ttagGATAGAAGATATTGAACATTTTTGTATTTGGTGGGGAGAGAGCTCAGAGGGAGGAAGAAATAGAAGATGCAGAAGAGGATGGACTAATTGATGGAGCAGAGTCTTTGAGgttaa"
    pi_dict = cpd.create_pi_dict(octamers_file_path)
    x_data, y_data = make_main_trace_data(fasta_seq, pi_dict)
    print([[x_data], [y_data]])

