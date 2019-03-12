import create_pi_dict as cpd
import matplotlib.pyplot as plt

def make_plot(pi_dict):

    # Read fasta file
    fasta_seq = "ttagGATAGAAGATATTGAACATTTTTGTATTTGGTGGGGAGAGAGCTCAGAGGGAGGAAGAAATAGAAGATGCAGAAGAGGATGGACTAATTGATGGAGCAGAGTCTTTGAGgttaa"
    fasta_seq = fasta_seq.lower()

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