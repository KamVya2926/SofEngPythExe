"""
This module translates an RNA sequence into its corresponding amino acid sequence.
It first finds the longest open reading frame and then uses this for translating.
Input: rna_sequence (str) containing only a, c, g, u
Output: aa_sequence (str) containing only the 20 common amino acid symbols in uppercase
"""

#import modules
from SEPythExe.logger import logger
from SEPythExe.utils.validateRNA import validate_rna
import re

#Codon table
codon_table = {
            "uuu": "F", "uuc": "F",
            "uua": "L", "uug": "L", "cuu": "L", "cuc": "L", "cua": "L", "cug": "L",
            "ucu": "S", "ucc": "S", "uca": "S", "ucg": "S", "agu": "S", "agc": "S",
            "uau": "Y", "uac": "Y",
            "uaa": "*", "uag": "*", "uga": "*",
            "ugu": "C", "ugc": "C",
            "ugg": "W",
            "ccu": "P", "ccc": "P", "cca": "P", "ccg": "P",
            "cau": "H", "cac": "H",
            "caa": "Q", "cag": "Q",
            "cgu": "R", "cgc": "R", "cga": "R", "cgg": "R", "aga": "R", "agg": "R",
            "auu": "I", "auc": "I", "aua": "I",
            "aug": "M",
            "acu": "T", "acc": "T", "aca": "T", "acg": "T",
            "aau": "N", "aac": "N",
            "aaa": "K", "aag": "K",
            "gau": "D", "gac": "D",
            "gaa": "E", "gag": "E",
            "guu": "V", "guc": "V", "gua": "V", "gug": "V",
            "gcu": "A", "gcc": "A", "gca": "A", "gcg": "A",
            "ggu": "G", "ggc": "G", "gga": "G", "ggg": "G"
        }


def find_longest_ORF(rna_sequence):
    ORFs = []

    # Regular expressions for start and stop codons
    start_codon = 'aug'
    stop_codons = ['uga', 'uaa', 'uag']

    # Loop through the sequence to find start codons
    for start_match in re.finditer(start_codon, rna_sequence):
        # From the position of the start codon, search for the closest stop codon
        for stop_codon in stop_codons:
            stop_match = re.search(stop_codon, rna_sequence[start_match.start():])
            if stop_match:
                # Get the ORF sequence from start codon to stop codon
                orf = rna_sequence[start_match.start():start_match.start() + stop_match.end()]

                # Check if the length of the ORF is divisible by 3 (valid ORF)
                if len(orf) % 3 == 0:
                    ORFs.append(orf)
                break  # Stop after finding the first stop codon

    if ORFs:
        # Sort the ORFs by length and return the longest ORF
        ORFs.sort(key=len, reverse=True)
        logger.info(f"The longest ORF is: {ORFs[0]}")
        return ORFs[0]
    else:
        logger.info("No valid ORF found")
        return None


def translate_rna_to_protein(rna_sequence):
    """
    Translates an RNA sequence into a protein sequence.
    """
    if validate_rna(rna_sequence): #check that the input is a string, only contains a, c, g, u characters,
                                    #and give a warning if a Thymine (T) is discovered, possibly indicating that the input is DNA and not RNA

        logger.info('Input is a valid RNA sequence')


    protein_sequence = []
    # Iterate over the RNA sequence in steps of 3 (codon length)
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i + 3]
        if codon in codon_table:
            # If the codon is in the table, append the corresponding amino acid
            amino_acid = codon_table[codon]
            if amino_acid == "*":
                # Stop codon found, stop translation
                break
            protein_sequence.append(amino_acid)
        else:
            # Invalid codon encountered (handle error or skip)
            logger.warning(f"Invalid codon {codon} encountered. Skipping.")
            continue

    return ''.join(protein_sequence)


# Example usage:
qs = "gcugagacuuccuggacgggggacaggcugugggguuucucagauaacugggccccugcgcucaggaggccuucacccucugcucuggguaaaguucauuggaacagaaagaaauggauuuaucugcucuucgcguugaagaaguacaaaaugucauuaaugcuaugcagaaaaucuuagagugucccaucugucuggaguugaucaaggaaccugucuccacaaagugugaccacauauuuugcaaauuuugcaugcugaaacuucucaaccagaagaaagggccuucacaguguccuuuauguaagaaugauauaaccaaaaggagccuacaagaaaguacgagauuuagucaacuuguugaagagcuauugaaaaucauuugugcuuuucagcuugacacagguuuggaguaugcaaacagcuauaauuuugcaaaaaaggaaaauaacucuccugaacaucuaaaagaugaaguuucuaucauccaaaguaugggcuacagaaaccgugccaaaagacuucuacagagugaacccgaaaauccuuccuugcaggaaaccagucucaguguccaacucucuaaccuuggaacugugagaacucugaggacaaagcagcggauacaaccucaaaagacgucugucuacauugaauugggaucugauucuucugaagauaccguuaauaaggcaacuuauugcagugugggagaucaag"
longest_orf = find_longest_ORF(qs)

if longest_orf:
    protein_sequence = translate_rna_to_protein(longest_orf)
    logger.info(f"The corresponding protein sequence is: {protein_sequence}")
    print(f"Protein Sequence: {protein_sequence}")

#qs = "gcugagacuuccuggacgggggacaggcugugggguuucucagauaacugggccccugcgcucaggaggccuucacccucugcucuggguaaaguucauuggaacagaaagaaauggauuuaucugcucuucgcguugaagaaguacaaaaugucauuaaugcuaugcagaaaaucuuagagugucccaucugucuggaguugaucaaggaaccugucuccacaaagugugaccacauauuuugcaaauuuugcaugcugaaacuucucaaccagaagaaagggccuucacaguguccuuuauguaagaaugauauaaccaaaaggagccuacaagaaaguacgagauuuagucaacuuguugaagagcuauugaaaaucauuugugcuuuucagcuugacacagguuuggaguaugcaaacagcuauaauuuugcaaaaaaggaaaauaacucuccugaacaucuaaaagaugaaguuucuaucauccaaaguaugggcuacagaaaccgugccaaaagacuucuacagagugaacccgaaaauccuuccuugcaggaaaccagucucaguguccaacucucuaaccuuggaacugugagaacucugaggacaaagcagcggauacaaccucaaaagacgucugucuacauugaauugggaucugauucuucugaagauaccguuaauaaggcaacuuauugcagugugggagaucaag"