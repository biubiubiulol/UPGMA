'''
Finds distance using Kimura's 2-Parameter metric
(Kimura, 1980)
'''
import math
import global_alignment as ga
import readfasta as r

#TODO: Alignment of the 2 sequences



def k2p(sequence_1, sequence_2):
    seq_list =  ga.align(sequence_1, sequence_2)
    seq1 = seq_list[0]
    seq2 = seq_list[1]
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
    }
    number_transitions = 0
    number_transversions = 0
    for base in range(len(seq1)):
        type1 = bases.get(seq1[base])
        type2 = bases.get(seq2[base])
        if seq1[base] != seq2[base]:
            if type1 == type2:
                number_transitions = number_transitions+1
            else:
                number_transversions = number_transversions+1
    s = number_transitions/length
    v = number_transversions/length
    print(s, v)
    d = -(0.5)*math.log(1- 2*s - v) - (0.25)*math.log(1- 2*v)

    return d

if __name__ == '__main__':
    s1 = r.readfasta("sample.fasta.txt")[0][1]
    s2 = r.readfasta("sample.fasta.txt")[1][1]
    k2p(s1,s2)
