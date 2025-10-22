"""
This module creates the complementary DNA sequence (cDNA) to a reverse (antisense) strand.
Input:Input: dna_sequence (str) containing only A, C, G, T
Output: complement_sequence (str) containing only A, C, G, T
"""

#import modules
from SEPythExe.logger import logger
from SEPythExe.utils.validateDNA import validate_dna
from SEPythExe.modules.reverse import reverse
from SEPythExe.modules.complement import complement

def reverse_complement(dna_sequence):
    if validate_dna(dna_sequence): # check that the input is a string, if it contains only ACTG characters,
                                # and give a warning if it contains uracil (U) using the validateDNA module
        logger.info('Input is a valid DNA sequence')


    complement_sequence = complement(dna_sequence) # create complementary strand using complement function from complement module
    reverse_comp = reverse(complement_sequence) # reverse the complementary strand using the reverse function from the reverse module
    logger.info(f"Complimentary DNA sequence of reverse strand: {reverse_comp}")
    return reverse_comp

#qs = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTAGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAAACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCAAAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAG"
#reverse_complement(qs)