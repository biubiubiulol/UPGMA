from sys import argv
from read_fasta import read_fasta
import numpy as np

'''
Shaban Agayev
A program that does a global alignment on two sequences.
'''

def align():
    s1 = 'CAGC'
    s2 = 'ACAGTA'

    s1_length = len(s1)
    s2_length = len(s2)

    gap_penalty = -7
    mismatch_penalty = -4
    match_bonus = 5

    scores = np.zeros(shape=(s1_length+1, s2_length+1))

    for i in range(1, s1_length+1):
        scores[i][0] = gap_penalty * i

    for j in range(0, s2_length+1):
        scores[0][j] = gap_penalty * j

    for i in range(1, s1_length+1):
        for j in range(1, s2_length+1):
            val1 = 0
            val2 = 0
            val3 = 0
            if s1[i-1] == s2[j-1]:
                val1 = scores[i-1][j-1] + match_bonus
            else:
                val1 = scores[i-1][j-1] + mismatch_penalty

            val2 = scores[i-1][j] + gap_penalty
            val3 = scores[i][j-1] + gap_penalty

            scores[i][j] = max(val1, val2, val3)

    print(scores)


'''
    seq1_align = ''
    seq2_align = ''

    i = s1_length
    j = s2_length

    print(scores)
    print("final")
    while i > 1 and j > 1:
        if scores[i][j] == ((scores[i-1][j-1]) - match_bonus) or ((scores[i-1][j-1]) - mismatch_penalty):
            seq1_align += s1[i-1]
            seq2_align += s2[j-1]
            i -= 1
            j -= 1
        elif scores[i][j] == (scores[i][j-1] - gap_penalty):
            seq1_align += s1[i-1]
            seq2_align += "-"
            j -= 1
        elif scores[i][j] == (scores[i-1][j] - gap_penalty):
            seq1_align += "-"
            seq2_align += s2[j-1]
            i -= 1
        else:
            print("error")
        print(scores)
        print(seq1_align)
        print(seq2_align)

    print(scores)
'''


def main():
    align()


main()

