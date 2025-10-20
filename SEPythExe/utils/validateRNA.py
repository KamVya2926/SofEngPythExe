"""
A utility to check if an RNA sequence is a string, in lowercase and only contains A, U, G, C characters. If a Thiamine (T) is found
then it gives a warning asking the user to check if the sequence is RNA or DNA
"""

from SEPythExe.logger import logger

valid_rna_bases = set("ACGU")

def validate_rna(rna_sequence):

    if not isinstance(rna_sequence, str): #checking if the input is a string
        logger.error("Input sequence must be a string") #If not, then it will give this error message

    if not rna_sequence.islower(): #checking if input is lowercase
        logger.error("Input sequence must be lowercase")

    if "T" in rna_sequence.lower(): #checking for "T/t", indicating the input might be DNA and not RNA
        logger.warning("Thiamine (T) found in sequence. Input must be RNA")

    #check for invalid characters, i.e. any other than ACGU
    invalid_bases = set(rna_sequence).difference(valid_rna_bases)
    if invalid_bases:
        logger.error(f"Input sequence contains invalid bases: {invalid_bases}. Use only A, C, G, U")
        raise ValueError("Input sequence contains invalid bases. Use only A, C, G, U " )
    return True