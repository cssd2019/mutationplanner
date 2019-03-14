import numpy

def combine_pi_score(oct_dict, strategy):
    """Takes in a dictionary (oct_dict) and returns a disctionry with the same keys,
     but with the new scores to be used for plot

    :param oct_dict (dict): a dictionary containing a list of P and I values for each octamer
    :param strategy (int): an integer (1, 2 or 3) . It Defines different strategies for calculating the new score
    :return: a dictionary of combined P and I values for all octamers
    """

    output_dict = {}
    for k, v in oct_dict.items():  # k = key (e.g. 'aaaaaaaa'), v = value
        i_inx = v[0]
        p_inx = v[1]
        if (strategy == 1):
            pi = combinePI_1(i_inx, p_inx)

        elif (strategy == 2):
            pi = combinePI_2(i_inx, p_inx)

        elif (strategy == 3):
            pi = combinePI_3(i_inx, p_inx)
        output_dict[k] = pi
    return output_dict


def combinePI_1(iindex, pindex):
    ''' Categorizing whether a octamer is a splicing enhancer, splicing inhibitor or neither
    Input: I-index (iindex) and P-index (pindex)
    output: 1 --> Splicing enhancer
            0 --> Neither
            -1 --> Splicing inhibitor

            999 --> Function did not do what it is supposed to, check code'''

    output_value = 999
    if iindex > 2.62 and pindex > 2.62:
        output_value = 1

    elif iindex < -2.62 and pindex < -2.62:
        output_value = -1

    else:
        output_value = 0

    if output_value == 999:
        print("Something is wrong, nothing happened")
        output_value = "Something is wrong, nothing happened"

    return output_value


def combinePI_2(iindex, pindex):
    ''' Categorizing whether a octamer is a splicing enhancer, splicing inhibitor or neither
    Input: I-index (iindex) and P-index (pindex)
    output: positive number (over 2.62) --> Splicing enhancer
            0 --> Neither
            negative number (under -2.62) --> Splicing inhibitor

            999 --> Function did not do what it is supposed to, check code'''
    output_value = numpy.mean([iindex, pindex])
    # output_value = 999
    # if iindex > 2.62 and pindex > 2.62:
    #     output_value = numpy.mean([iindex, pindex])
    #
    # elif iindex < -2.62 and pindex < -2.62:
    #     output_value = numpy.mean([iindex, pindex])
    #
    # else:
    #     output_value = 0
    #
    # if output_value == 999:
    #     print("Something is wrong, nothing happened")
    #     output_value = "Something is wrong, nothing happened"

    return output_value

def combinePI_3(iindex, pindex):
    ''' Categorizing whether a octamer is a splicing enhancer, splicing inhibitor or neither
    Input: I-index (iindex) and P-index (pindex)
    output: positive number --> Splicing enhancer
            0 --> Neither
            Negative number --> Splicing inhibitor

            999 --> Function did not do what it is supposed to, check code'''

    output_value = 999
    if iindex > 2.62 and pindex > 2.62:
        output_value = (iindex - 2.62) + (pindex - 2.62)

    elif iindex < -2.62 and pindex < -2.62:
        output_value = (iindex + 2.62) + (pindex + 2.62)

    else:
        output_value = 0

    if output_value == 999:
        print("Something is wrong, nothing happened")
        output_value = "Something is wrong, nothing happened"

    return output_value


# UNIT TESTING with pytest
def test_combine_pi_score():
    # testing strategy 1
    dummy_dict = {'aaaaaaaa': [- 4.3231, - 5.252],
                  'aaaaaaca': [- 3.1298, - 3.5631],
                  'whatever': [1, 4],
                  'abababab': [4, 3]}

    t = combine_pi_score(dummy_dict, 1)

    assert t['aaaaaaaa'] == -1
    assert t['whatever'] == -0
    assert t['abababab'] == 1

    # testing strategy 2
    dummy_dict = {'aaaaaaaa': [- 4.62, - 5.62],
                  'aaaaaaca': [- 3.1298, - 3.5631],
                  'whatever': [1, 4],
                  'abababab': [4.62, 3.62]}

    t = combine_pi_score(dummy_dict, 2)

    assert t['aaaaaaaa'] == -5.12
    assert t['whatever'] == -0
    assert t['abababab'] == 4.12

    # testing strategy 3
    dummy_dict = {'aaaaaaaa': [- 4.62, - 5.62],
                  'aaaaaaca': [- 3.1298, - 3.5631],
                  'whatever': [1, 4],
                  'abababab': [4.62, 3.62]}

    t = combine_pi_score(dummy_dict, 3)

    assert t['aaaaaaaa'] == -5
    assert t['whatever'] == -0
    assert t['abababab'] == 3

