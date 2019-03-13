import make_main_trace_data as mmtd
import create_pi_dict as cpd
import matplotlib.pyplot as plt
import numpy as np

## GLOBAL ###
octamers_file_path = "./data/octamers.txt"
fasta_seq = "ttagGATAGAAGATATTGAACATTTTTGTATTTGGTGGGGAGAGAGCTCAGAGGGAGGAAGAAATAGAAGATGCAGAAGAGGATGGACTAATTGATGGAGCAGAGTCTTTGAGgttaa"
pi_dict = cpd.create_pi_dict(octamers_file_path)
#############

def make_mutation_data(mutation_base_index, new_base):
    new_base = new_base.lower()
    new_fasta_seq = fasta_seq[0:mutation_base_index] + new_base +  fasta_seq[mutation_base_index+1: ]
    new_fasta_seq = new_fasta_seq.lower()
    x_data, y_data = mmtd.make_main_trace_data(new_fasta_seq, pi_dict)
    print(fasta_seq)    
    print(new_fasta_seq)  
    return x_data, y_data

def print_object_methods(object):
    object_methods = [method_name for method_name in dir(object)
                      if callable(getattr(object, method_name))]
    print(object_methods)

def onpick(event):
    txt = event.artist
    print_object_methods(txt)
    #print_object_methods(event)
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
    mutation_base_index, _= txt.get_position()
    new_x_data, new_y_data = make_mutation_data(mutation_base_index, new_txt)
    plt.plot(new_x_data, new_y_data, '-', linewidth=2, markersize=12, color=new_color)

    # refresh the figure
    event.canvas.draw_idle()
    

def make_plot(x_data, y_data, fasta_seq):
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
    fig.canvas.mpl_connect('pick_event', onpick)
    plt.show()





if __name__ == "__main__":
    octamers_file_path = "./data/octamers.txt"
    fasta_seq = "ttagGATAGAAGATATTGAACATTTTTGTATTTGGTGGGGAGAGAGCTCAGAGGGAGGAAGAAATAGAAGATGCAGAAGAGGATGGACTAATTGATGGAGCAGAGTCTTTGAGgttaa"

    pi_dict = cpd.create_pi_dict(octamers_file_path)
    x_data, y_data = mmtd.make_main_trace_data(fasta_seq, pi_dict)
    make_plot(x_data, y_data, fasta_seq)