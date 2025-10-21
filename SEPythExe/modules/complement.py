"""
This module creates the complimentary DNA strand to an input DNA sequence
Input:Input: dna_sequence (str) containing only A, C, G, T
Output: complement_sequence (str) containing only A, C, G, T
"""

#import modules
from SEPythExe.logger import logger
from SEPythExe.utils.validateDNA import validate_dna

def complement(dna_sequence):
    # check that the input is a string, if it contains only ACTG characters, and whether it contains uracil using the validateDNA module
    if validate_dna(dna_sequence):
        logger.info('Input is a valid DNA sequence')