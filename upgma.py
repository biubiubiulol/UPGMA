'''
This program should take the distance table of k2p with different sequences.
'''

import sys

newick_format = []


def main():
    sequences = ['A', 'B', 'C', 'D']
    table = {}
    for sequence in sequences:
        row = {}
        for col in sequences:
            row[col] = -1
        table[sequence] = row
    table['A']['A'] = 0
    table['A']['B'] = 13
    table['A']['C'] = 11
    table['A']['D'] = 7
    table['B']['A'] = 13
    table['B']['B'] = 0
    table['B']['C'] = 2
    table['B']['D'] = 11
    table['C']['A'] = 11
    table['C']['B'] = 2
    table['C']['C'] = 0
    table['C']['D'] = 9
    table['D']['A'] = 7
    table['D']['B'] = 11
    table['D']['C'] = 9
    table['D']['D'] = 0
    find_smallest(table)


def find_smallest(table):
    while len(table) > 2:
        minimum = sys.maxsize
        result = []
        for row in table:
            for col in table[row]:
                if table[row][col] < minimum and table[row][col] != 0 and table[row][col] != -1:
                    result = [row, col]
                    minimum = table[row][col]
        print(minimum)
        newick_format.append(result)
        print(newick_format)
        # remake both new sequence and new table
        table = remake_sequence(table, result)


def remake_sequence(table, result):
    sequences = list(table.keys())
    new_sequence = []
    # init new sequence
    for sequence in sequences:
        if sequence == result[0]:
            new_sequence.append(result[0] + result[1])
            continue
        elif sequence == result[1]:
            continue
        new_sequence.append(sequence)
    return remake_table(table, new_sequence, result)


def remake_table(table, new_sequences, result):
    new_table = {}
    # Init new table
    for new_sequence in new_sequences:
        row = {}
        for col in new_sequences:
            row[col] = 0
        new_table[new_sequence] = row

    for row in new_table:
        for col in new_table[row]:
            if row in table and col in table[row]:
                new_table[row][col] = table[row][col]
            elif col == result[0] + result[1] and col != row:
                new_table[row][col] = find_distance(table, result, row)
            elif row == result[0] + result[1] and col != row:
                new_table[row][col] = find_distance(table, result, col)
    print(new_table)
    return new_table


def find_distance(table, result, row):
    distance = (table[row][result[0]] + table[row][result[1]]) / 2
    return distance


if __name__ == '__main__':
    main()
