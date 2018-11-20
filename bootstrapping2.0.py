'''
Shaban Aagayev
Executes bootstrapping on sequences
Last modified: 19 November 2018
'''

from readfasta import readfasta
import random


def bootstrap():
    sequences = readfasta("mt_homo_dna.fasta")

    list_original_sequences = []
    for sequence in range(0, len(sequences)):  #convert (list of lists) to (list of strings), makes logic easier later
        list_original_sequences.append(sequences[sequence][1])

    print("Original Sequences")

    for sequence in range(0, len(list_original_sequences)):
        print(list_original_sequences[sequence])

    i = 0  #counter for number of letters appended
    j = len(min(list_original_sequences, key=len))  #num of letters needed to be appended, shortest string in orig. seqs
    k = len(list_original_sequences)-1  #number of sequences
    new_sequences = [""] * k  #generates k number of empty strings, stores in list

    while i != j:
        random_num = random.randint(0, j-1)  #select random column

        for sequence in range(0,k):  #iterate thru total num of sequences
            new_sequences[sequence] += list_original_sequences[sequence][random_num]  #appends each sequence, each iter.
        i += 1

    print("New Sequences")

    for sequence in range(0, len(new_sequences)):
        print(new_sequences[sequence])


def main():
    bootstrap()


main()
