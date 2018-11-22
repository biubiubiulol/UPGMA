import numpy as np

'''
Shaban Agayev
A program that does a global alignment on two sequences.
'''


def align(s1, s2):
    s1_length = len(s1)
    s2_length = len(s2)

    gap_penalty = np.int32(-7)
    mismatch_penalty = np.int32(-4)
    match_bonus = np.int32(5)

    scores = np.zeros(shape=(s1_length + 1, s2_length + 1), dtype=np.int32)

    for i in range(1, s1_length+1):
        scores[i][0] = gap_penalty * i

    for j in range(1, s2_length+1):
        scores[0][j] = gap_penalty * j

    # matrix filling loop
    for i in range(1, s1_length+1):
        s1i = s1[i-1]
        scores_i = scores[i]
        scores_minus = scores[i-1]
        for j in range(1, s2_length+1):
            scores_minus_j_ = scores_minus[j - 1]
            if s1i == s2[j-1]:
                val1 = scores_minus_j_ + match_bonus
            else:
                val1 = scores_minus_j_ + mismatch_penalty

            val2 = scores_minus[j] + gap_penalty
            val3 = scores_i[j-1] + gap_penalty

            scores_i[j] = max(val1, val2, val3)

    seq1_align = ''
    seq2_align = ''

    i = s1_length
    j = s2_length

    while i > 0 and j > 0:
        if (scores[i][j]) == ((scores[i-1][j-1]) + match_bonus):
            seq1_align += s1[i-1]
            seq2_align += s2[j-1]
            i -= 1
            j -= 1
        elif scores[i][j] == ((scores[i][j-1]) + gap_penalty):
            seq1_align += "-"
            seq2_align += s2[j-1]
            j -= 1
        elif scores[i][j] == ((scores[i-1][j]) + gap_penalty):
            seq1_align += s1[i-1]
            seq2_align += "-"
            i -= 1
        elif scores[i][j] == ((scores[i - 1][j - 1]) + mismatch_penalty):
            seq1_align += s1[i-1]
            seq2_align += s2[j-1]
            i -= 1
            j -= 1

    while i != 0:
        seq1_align += s1[i-1]
        seq2_align += "-"
        i -= 1

    while j != 0:
        seq2_align += s2[j - 1]
        seq1_align += "-"
        j -= 1

    return [seq1_align[::-1], seq2_align[::-1]]
