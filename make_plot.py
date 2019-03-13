import matplotlib.pyplot as plt
import numpy as np
import make_trace_data as mtd


def _make_mutated_data(mutation_base_index, new_base, fasta_seq, pi_dict):
    """Internal helper function to make mutated trace data

    :param mutation_base_index (int): the index of the base that is mutated
    :param new_base (string): the base (A, T, C, or G) itself that is mutated
    :param fasta_seq (string): the fasta sequence
    :param pi_dict (dict): dictionary of combined P and I values for all octamers
    :return: two numpy arrays (the first array contains x_axis data, and the second contains y_axis data)
    """
    new_base = new_base.lower()
    new_fasta_seq = fasta_seq[0:mutation_base_index] + new_base +  fasta_seq[mutation_base_index+1: ]
    new_fasta_seq = new_fasta_seq.lower()
    x_data, y_data = mtd.make_trace_data(new_fasta_seq, pi_dict)
    print(fasta_seq)
    print(new_fasta_seq)
    return x_data, y_data

def _print_object_methods(object):
    """Internal helper function to return methods of an object

    :param object: object whose methods should be printed
    :return: None
    """
    object_methods = [method_name for method_name in dir(object)
                      if callable(getattr(object, method_name))]
    print(object_methods)


def _onclick(event, fasta_seq, pi_dict):
    """Internal helper function that handles the clicks on the nucleotides,
    mutates the nucleotide, and also adds a trace on the plot to show the effect of
    the mutation.

    :param event (object): event data passed by the picker
    :param fasta_seq (string): the fasta sequence
    :param pi_dict (dict): dictionary of combined P and I values for all octamers
    :return: None
    """
    txt = event.artist
    #_print_object_methods(txt)
    #_print_object_methods(event)
    #print(vars(event))
    current_text = txt.get_text()

    # transitions: get new base and its color
    # A --> T --> C --> G --> A and so on
    if current_text == 'A':
        new_txt = 'T'
        new_color = 'y'
    elif current_text == 'T':
        new_txt = 'C'
        new_color = 'g'
    elif current_text == 'C':
        new_txt = 'G'
        new_color = 'b'
    elif current_text == 'G':
        new_txt = 'A'
        new_color = 'r'
    txt.set_text(new_txt)
    txt.set_color(new_color)

    # get the index of the mutated base and recompute the graph data
    mutation_base_index, _ = txt.get_position()
    new_x_data, new_y_data = _make_mutated_data(mutation_base_index, new_txt, fasta_seq, pi_dict)

    # plot mutated trace
    plt.plot(new_x_data, new_y_data, '-', linewidth=2, markersize=12, color=new_color)

    # refresh the figure
    event.canvas.draw_idle()


def make_plot(x_data, y_data, fasta_seq, pi_dict):
    """This function makes the main plot

    :param x_data (numpy array): contains data to plot on the x-axis
    :param y_data: (numpy array): contains data to plot on the y-axis
    :param fasta_seq: (string): fasta sequence for annotation the line plot
    :param pi_dict (dict): dictionary of combined P and I values for all octamers
    :return: None
    """
    fig = plt.figure(figsize=[12, 5])
    plt.plot(x_data, y_data, '-', linewidth=2, markersize=12)

    y_data_min = np.nanmin(y_data)
    y_data_max = np.nanmax(y_data)

    for idx, base in enumerate(fasta_seq):
        x = x_data[idx]
        th = plt.text(x, y_data_min-4, base.upper(), fontsize=8, picker=5)
        th.old_value = base.upper()

    #plt.xlim(left=-1, right=10)
    plt.ylim(bottom=y_data_min-8, top=y_data_max+4)
    fig.canvas.mpl_connect('pick_event', lambda event: _onclick(event, fasta_seq, pi_dict))
    plt.show()


if __name__ == "__main__":
    import create_pi_dict as cpd
    octamers_file_path = "./data/octamers.txt"
    fasta_seq = "ttagGATAGAAGATATTGAACATTTTTGTATTTGGTGGGGAGAGAGCTCAGAGGGAGGAAGAAATAGAAGATGCAGAAGAGGATGGACTAATTGATGGAGCAGAGTCTTTGAGgttaa"
    pi_dict = cpd.create_pi_dict(octamers_file_path)
    x_data, y_data = mtd.make_trace_data(fasta_seq, pi_dict)
    make_plot(x_data, y_data, fasta_seq, pi_dict)