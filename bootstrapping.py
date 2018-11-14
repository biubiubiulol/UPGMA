import readfasta
import numpy as np


def main():
    dna = ["ABCDEFG", "ABDCEGF", "ACBDEGF"]
    new_sequences = []
    for sequence in dna:
        new_sequences.append(list(sequence))
    new_sequences = np.array(new_sequences)
    print(new_sequences)


if __name__ == '__main__':
    main()
