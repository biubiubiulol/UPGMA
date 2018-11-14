import readfasta
import numpy as np
import random


def main():
    dna = ["ABCDEFG", "ABDCEGF", "ACBDEGF"]
    new_sequences = []
    for sequence in dna:
        new_sequences.append(list(sequence))
    new_sequences = np.array(new_sequences)
    print(new_sequences)
    random_list = []

    for i in range(len(new_sequences[0])):
        random_list.append(random.randint(0, len(new_sequences) - 1))
    print(random_list)
    random_sequences = np.empty((len(new_sequences[0]), len(new_sequences[0])))

    for i in range(len(random_list)):
        np.insert(random_sequences, i, new_sequences[:0], 1)



if __name__ == '__main__':
    main()
