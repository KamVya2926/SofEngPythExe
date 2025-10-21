"""
This is a module that transcribes a DNA sequence into the corresponding mRNA sequence, converting all thymine (T) to uracil (u) and enforcing lowercase alphabet.
Input: dna_sequence (str) containing only A, C, G, T
Output: mRNA_sequence (str) containing only a, c, g, u
"""

#import modules
from SEPythExe.logger import logger
from SEPythExe.utils.validateDNA import validate_dna
from SEPythExe.utils.validateRNA import validate_rna


def transcribe_dna_sequence(dna_sequence):
# check that the input is a string, if it contains only ACTG characters, and whether it contains uracil using the validateDNA module
    if validate_dna(dna_sequence):
        logger.info('Input is a valid DNA sequence')


    #transcribe the input sequence to RNA
    dna_sequence = "".join(dna_sequence.split()) #clean the input DNA sequence by removing whitespaces (spaces, newlines, tabs)
    rna_sequence = dna_sequence.replace("T", "U").lower() # Replace all Thymine (T) with Uracil (u) and enforce lowercase alphabet
    logger.info('Transcribing DNA sequence to RNA')

    if validate_rna(rna_sequence):
        logger.info(f"Successfully transcribed input DNA sequence to a valid RNA sequence: {rna_sequence}")

    return rna_sequence


qs = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTAGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAAACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCAAAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAG"
transcribe_dna_sequence(qs)