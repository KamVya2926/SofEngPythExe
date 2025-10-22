"""
This module creates the complimentary DNA strand (cDNA) to an input DNA sequence
Input: dna_sequence (str) containing only A, C, G, T
Output: complement_sequence (str) containing only A, C, G, T
"""

#import modules
from SEPythExe.logger import logger
from SEPythExe.utils.validateDNA import validate_dna


base_complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} #Create dictionary to define the complement bases

def complement(dna_sequence):
    if validate_dna(dna_sequence): # check that the input is a string, if it contains only ACTG characters,
                                   # and give a warning if it contains uracil (U) using the validateDNA module

        logger.info('Input is a valid DNA sequence')

    c_dna = '' #initialise the list to contain the complimentary bases

    for base in dna_sequence: #for loop going through input DNA sequence
        c_dna += base_complement[base] #Matching the complimentary base according to the base_complement dictionary and adding to the c_dna list
        logger.info(f"Complimentary DNA sequence: {c_dna}")

    return c_dna


#qs = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTAGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAAACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCAAAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAG"
#complement(qs)