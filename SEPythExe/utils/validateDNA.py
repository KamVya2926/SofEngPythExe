"""
A utility to check if an DNA sequence is a string, in uppercase and only contains ATGC characters. If a Uracil (U) is found
then it gives a warning asking the user to check if the sequence is DNA or RNA
"""

from SEPythExe.logger import logger

valid_dna_bases = set("ACGT")

def validate_dna(dna_sequence):

    if not isinstance(dna_sequence, str): #checking if the input is a string
        logger.error("Input sequence must be a string") #If not, then it will give this error message

    if not dna_sequence.isupper(): #checking if input is uppercase
        logger.error("Input sequence must be uppercase")

    if "u" in dna_sequence.lower(): #checking for "U/u", indicating the input might be RNA and not DNA
        logger.warning("Uracil (U) found in sequence. Input must be DNA")

    #check for invalid characters, i.e. any other than ACGT
    invalid_bases = set(dna_sequence).difference(valid_dna_bases)
    if invalid_bases:
        logger.error(f"Input sequence contains invalid bases: {invalid_bases}. Use only A, C, G, T")
        raise ValueError("Input sequence contains invalid bases. Use only A, C, G, T " )
    return True
