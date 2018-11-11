'''
This program should take the distance table of k2p with different sequences.
'''

import sys
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
    table['B']['B'] = 0
    table['B']['C'] = 2
    table['B']['D'] = 11
    table['C']['C'] = 0
    table['C']['D'] = 9
    table['D']['D'] = 0

    print(find_smallest(table))


def find_smallest(table):
    minimum = sys.maxsize
    result = []
    for row in table:
        for col in table[row]:
            if table[row][col] < minimum and table[row][col] != 0 and table[row][col] != -1:
                result = [row, col]
                minimum = table[row][col]
    print(minimum)
    return result


if __name__ == '__main__':
    main()
