def convert_fasta_case(seq_dict):
    """Loops over fasta dictionary and coverts all the fasta records
    to lower case.
    :param seq_dict (dict): a dictionary of fasta sequence IDs and sequences
    :return: a dictionary of fasta record
    """
    for k, v in seq_dict.items():
        seq_dict[k] = v.lower()

    return seq_dict


if __name__ == "__main__":
    import read_fasta as rf
    fasta_file_path = "./data/test.fasta"
    fasta_dict = rf.read_fasta(fasta_file_path)
    print(fasta_dict)
    fasta_dict = convert_fasta_case(fasta_dict)
    print(fasta_dict)
