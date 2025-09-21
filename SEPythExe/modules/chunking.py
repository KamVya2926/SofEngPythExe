"""
This function is called chunking. It does the following:
1. Takes a string (str) and a chunk size (c).
2.Breaks the string into chunks of chunk_size.
3. Prints the chunks in one line separated by a comma and a space.
"""

# Import these modules
import SEPythExe.logger

def chunking(str, cs): #define the function.
    chunks = [] #Initialise a list to contain the chunks (substrings)
    for i in range(0, len(str), cs): #for loop going through the input string, starting at 0 upto the end in chunks set by the cs variable
        chunks.append(str[i:i+cs]) # Add (append) the chunks to the chunks list
    return ' '.join(chunks) #returns list of chunks, with chunks separated by a space


#Example
#str:
s= "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"
#cs:
k= 10
print(chunking(s, k))

#output:
#GCTGAGACTT CCTGGACGGG GGACAGGCTG TGGGGTTTCT CAGATAACTG GGCCCCTGCG CTCAGGAGGC CTTCACCCTC TGCTCTGGGT AAAGTTCATT GGAACAGAAA GAAATGGATT TATCTGCTCT TCGCGTTGAA GAAGTACAAA ATGTCATTAA TGCTATGCAG AAAATCTTAG AGTGTCCCAT CTGTCTGGAG TTGATCAAGG AACCTGTCTC CACAAAGTGT GACCACATAT TTTGCAAATT TTGCATGCTG AAACTTCTCA ACCAGAAGAA AGGGCCTTCA CAGTGTCCTT TATGTAAGAA TGATATAACC AAAAGGAGCC TACAAGAAAG TACGAGATTT GAT