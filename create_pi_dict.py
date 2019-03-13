def create_pi_dict(file_path):
    """Reads Octamers file and creates a dictionary of P and I values for each octamer.

    :param file_path (string): Path of the file containing P and I values for all octamers
    :return: A dictionary containing a list of PI values for each octamer
    """
    pi_dict = dict()

    with open(file_path) as file:
        # ignore the header section containing bullshit
        while True:
            current_line = file.readline()
            if current_line == "Octamer \tP-index  I-index\n":
                break

        # make dictionary of the P and I values
        i = 0
        while True:
            i += 1
            current_line = file.readline()
            if current_line == '':
                print("Reached the end of the file.")
                break
            else:
                # sometime there is an empty line that can't be split
                # so catch and ignore these lines
                try:
                    (key, p_value, i_value) = current_line.split()
                    pi_dict[key] = [float(p_value), float(i_value)]
                except:
                    print('Warning: Encountered an empty line in the data.')
    return pi_dict


def test_create_pi_dict():
    expected = {'aaaaaaaa': [- 4.3231, - 5.252],
                'aaaaaaca': [- 3.1298, - 3.5631]
                }
    assert create_pi_dict("./data/test_octamers.txt") == expected


if __name__ == "__main__":
    file_path = "./data/octamers.txt"
    pi_dict = create_pi_dict(file_path)
    print(pi_dict)