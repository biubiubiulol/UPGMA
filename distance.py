'''
Finds distance using Kimura's 2-Parameter metric
(Kimura, 1980)
'''
import math

#TODO: Alignment of the 2 sequences

def align(seq1, seq2):
    #get rid of this once done
    print("This is placeholder for a function implementing dynamic programming")
    #once this is made actually return the proper output values
    return seq1, seq2


def k2p(sequence_1, sequence_2):
    seq_list =  align(sequence_1, sequence_2)
    seq1 = seq_list[1]
    seq2 = seq_list[2]
    alpha = 0.9
    beta = 0.1
    if len(seq1) >= len(seq2):
        length = len(seq1)
    else:
        length = len(seq2)
    #we could do alpha = 0.95, beta = 0.05 as suggested in
    #the literature.
    bases = {
        "A" : 0,
        "G" : 0,
        "C" : 1,
        "T" : 1,
        "-" : -1,
    }
    number_transitions = 0
    number_transversions = 0
    for base in range(len(seq1)):
        type1 = bases.get(seq1[base])
        type2 = bases.get(seq2[base])
        if seq1[base] != seq2[base]:
            if type1 != -1 or type2 != -1:
                if type1 == type2:
                    number_transitions = number_transitions+1
                elif type1 != type2:
                    number_transversions = number_transversions+1
    s = number_transitions/length
    v = number_transversions/length
    d = -(.5)*math.log(1- 2*s - v) - (0.25)*math.log(1- 2*v) 
    return d
