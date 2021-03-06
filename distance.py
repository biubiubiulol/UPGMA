'''
William Bordowitz and Spencer Berg
Finds distance using Kimura's 2-Parameter metric
(Kimura, 1980)
'''
import math
import readfasta as r
import global_alignment as ga
import multiprocessing as mp


def k2p(sequence_1, sequence_2):
    if sequence_1 == sequence_2:
        return 0
    seq_list = ga.align(sequence_1, sequence_2)
    seq1 = seq_list[0]
    seq2 = seq_list[1]
    print(seq1 + '\n' + seq2)
    if len(seq1) >= len(seq2):
        length = len(seq1)
    else:
        length = len(seq2)
    bases = {
        "A": 0,
        "G": 0,
        "C": 1,
        "T": 1,
        "-": -1,
    }
    number_transitions = 0
    number_transversions = 0
    for base in range(len(seq1)):
        type1 = bases[seq1[base]]
        type2 = bases[seq2[base]]
        if seq1[base] != seq2[base]:
            if type1 != -1 and type2 != -1:
                if type1 == type2:
                    number_transitions = number_transitions + 1
                elif type1 != type2:
                    number_transversions = number_transversions + 1
    s = number_transitions / length
    v = number_transversions / length
    print(s, v)
    d = -.5 * math.log(1 - 2 * s - v) - 0.25 * math.log(1 - 2 * v)
    print(d)
    return d


def k2p_multiprocess(seq1, seq2):
    return [seq1[0], seq2[0], k2p(seq1[1], seq2[1])]


def get_k2p_table(sequence_list):
    thread_count = 2
    size = len(sequence_list)
    table = dict()
    processes = mp.Pool(processes=thread_count)
    process_pool = []
    for seq in sequence_list:
        table[seq[0]] = dict()
    for i in range(size):
        seq1 = sequence_list[i]
        for j in range(i, size):
            seq2 = sequence_list[j]
            process_pool.append(processes.apply_async(k2p_multiprocess, (seq1, seq2,)))
    processes.close()
    processes.join()
    for p in process_pool:
        result = p.get()
        s1name = result[0]
        s2name = result[1]
        distance = result[2]
        table[s1name][s2name] = distance
        table[s2name][s1name] = distance

    return table


if __name__ == '__main__':
    sq1 = r.readfasta("sample.fasta.txt")[0][1]
    sq2 = r.readfasta("sample.fasta.txt")[1][1]
    k2p(sq1, sq2)
