'''
This program should take the distance table of k2p with different sequences.
'''

import sys
import distance as d
import readfasta


def main():
    #sequences = readfasta.readfasta("filename")
    sequences = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
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
    table['A']['E'] = 12
    table['A']['F'] = 16
    table['A']['G'] = 15
    table['B']['A'] = 13
    table['B']['B'] = 0
    table['B']['C'] = 2
    table['B']['D'] = 11
    table['B']['E'] = 14
    table['B']['F'] = 13
    table['B']['G'] = 5
    table['C']['A'] = 11
    table['C']['B'] = 2
    table['C']['C'] = 0
    table['C']['D'] = 9
    table['C']['E'] = 18
    table['C']['F'] = 15
    table['C']['G'] = 3
    table['D']['A'] = 7
    table['D']['B'] = 11
    table['D']['C'] = 9
    table['D']['D'] = 0
    table['D']['E'] = 8
    table['D']['F'] = 14
    table['D']['G'] = 13
    table['E']['A'] = 12
    table['E']['B'] = 14
    table['E']['C'] = 18
    table['E']['D'] = 8
    table['E']['E'] = 0
    table['E']['F'] = 18
    table['E']['G'] = 13
    table['F']['A'] = 16
    table['F']['B'] = 13
    table['F']['C'] = 15
    table['F']['D'] = 14
    table['F']['E'] = 18
    table['F']['F'] = 0
    table['F']['G'] = 14
    table['G']['A'] = 15
    table['G']['B'] = 5
    table['G']['C'] = 3
    table['G']['D'] = 13
    table['G']['E'] = 13
    table['G']['F'] = 14
    table['G']['G'] = 0
    global help_table
    help_table = table

    find_smallest(table)


def find_smallest(table):
    newick_format = []
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
        # remake both new sequence and new table
        table = remake_sequence(table, result)
    print(newick_format)


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
    result_string = ''.join(result)
    distance = 0
    for char in result_string:
        for row_char in row:
            distance += help_table[row_char][char]
    # distance = (table[row][result[0]] + table[row][result[1]]) / 2
    return distance / (len(result_string) * len(row))


if __name__ == '__main__':
    main()
