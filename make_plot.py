import make_main_trace_data as mmtd
import create_pi_dict as cpd
import matplotlib.pyplot as plt
import numpy as np

def onpick(event):
    txt = event.artist
    print('clicked')


def make_plot(x_data, y_data):
    fig = plt.figure(figsize=[12, 5])
    plt.plot(x_data, y_data, '-', linewidth=2, markersize=12)
    
    # for figure adjustment
    y_data_min = np.nanmin(y_data)
    y_data_max = np.nanmax(y_data)

    # plot the sequence one base at a time
    for idx, base in enumerate(fasta_seq):
        x = x_data[idx]
        th = plt.text(x, y_data_min-4, base.upper(), fontsize=12, picker=5)

    # set proper limits so that the sequence is always visible below the trace
    #plt.xlim(left=-1, right=10)
    plt.ylim(bottom=y_data_min-8, top=y_data_max+4)
    print(y_data_min, y_data_max )
    fig.canvas.mpl_connect('pick_event', onpick)
    plt.show()


if __name__ == "__main__":
    octamers_file_path = "./data/octamers.txt"
    fasta_seq = "ttagGATAGAAGATATTGAACATTTTTGTATTTGGTGGGGAGAGAGCTCAGAGGGAGGAAGAAATAGAAGATGCAGAAGAGGATGGACTAATTGATGGAGCAGAGTCTTTGAGgttaa"
    pi_dict = cpd.create_pi_dict(octamers_file_path)
    x_data, y_data = mmtd.make_main_trace_data(fasta_seq, pi_dict)
    make_plot(x_data, y_data)