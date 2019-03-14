from Bio import SeqIO, Seq


def read_fasta(file_path):
    """ Reads a fasta file and converts it into a dictionary
    :param file_path (string): path of the fasta file to read
    :return: a dictionary of fasta records
    """
    seq_dict = {}
    for sequence in SeqIO.parse(file_path, "fasta"):  #
        s = str(sequence.seq)
        seq_dict[sequence.id] = s
    return seq_dict


if __name__ == "__main__":
    fasta_file_path = "./data/test.fasta"
    fasta_dict = read_fasta(fasta_file_path)
    print(fasta_dict)
