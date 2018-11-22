'''
This program should take the distance table of k2p with different sequences.
'''

import sys
import distance as d
import readfasta


def main():
    sequences = readfasta.readfasta(sys.arv[1])
    # sequences = readfasta.readfasta("mt_homo_dna.fasta")
    table = d.get_k2p_table(sequences)
    global help_table
    help_table = table

    find_smallest(table)


def find_smallest(table):
    while len(table) >= 2:
        minimum = sys.maxsize
        result = []
        for i in table.keys():
            row = table[i]
            for j in row.keys():
                value = row[j]
                if value < minimum and value != 0:
                    result = [i, j]
                    minimum = table[i][j]
        print(minimum)
        # add this as the root of the tree
        # newick_format.append(result)
        # remake both new sequence and new table
        table = remake_table(table, result)
    for key in table.keys():
        print(key)


def remake_table(table, result):
    seq1 = result[0]
    seq2 = result[1]
    combined_sequence = "(" + seq1 + "," + seq2 + ")"
    # use new sequence thing to make table rows and columns
    table[combined_sequence] = table[seq1]
    # set new distances for all values in row
    for key in table[combined_sequence].keys():
        if table[combined_sequence][key] != 0:
            avg_dist = find_avg_distance(table, result, seq1)
            table[combined_sequence][key] = avg_dist
            table[key][combined_sequence] = avg_dist

    # finally delete old ones
    del table[seq1]
    del table[seq2]
    for rowkey in table.keys():
        row = table[rowkey]
        colkeys = list(row.keys())
        for colkey in colkeys:
            if colkey == seq1 or colkey == seq2:
                del table[rowkey][colkey]
                pass
    return table


def find_avg_distance(table, result, row):
    distance = (table[row][result[0]] + table[row][result[1]]) / 2
    return distance


if __name__ == '__main__':
    main()
