"""
This function is called genbank_format. It does the following:
1. Takes a string (query_seq) and a chunk size (chunk_size), which is set at 10 characters.
2.Breaks the string into chunks of chunk_size.
3. Prints the output in the format of GenBank DNA sequence entries. So,
    6 chunks per line (ignoring everything apart from letters, and always in lower case - line 15)
    with each line prefixed with the number of the first character in the line
    based on its order in the original string.

"""
# Import these modules
from SEPythExe.logger import logger

def genbank_format(query_seq, chunk_size= 10):
    logger.debug(f"Function called with query_seq='{query_seq[:50]}...', chunk_size={chunk_size}") #Logs message at debug level. Takes first 50 characters of query sequence - whole sequence not taken so logs are not filled with huge amounts of data.
                                                                                                    #Wraps substring in quotes and adds '...' to indicate that the string has been truncated
    if not query_seq:
        logger.error("Empty input received.")
        return ""

    query_seq = ''.join([char for char in query_seq if char.isalpha()]).lower()
    logger.debug(f"Cleaned sequence: '{query_seq[:50]}...'")

    chunks = [] #initialise an empty list to store the chunks

#Nested for loop
#First loop going through query_seq in steps set by chunk_size to extract chunks of same size
#Chunks will be appended to chunks list
#Output will be all chunks in one line
    for i in range(0, len(query_seq), chunk_size):
        chunks.append(query_seq[i:i+chunk_size])


#Second for loop going thorough substrings in chunks list
#Starts from 0 going up to number of chunks set by len(chunks) in batches of 6
#(f"{start_index:>3}:" prints index of the first character in the line right-aligned followed by a colon
# Prints batches on separate lines with chunks separated by a space


    output_lines = [] #Initialise a list to contain the batches of chunks
    for i in range(0, len(chunks), 6):
        start_index = i * chunk_size+ 1  # Index of the first character in this line, starting at 1
        line_chunks = chunks[i:i + 6] #Batch of chunks assigned to variable
        line = f"{start_index:>3}: {' '.join(line_chunks)}"
        output_lines.append(line) #Append (add) the batches of chunks to the list

    logger.info(f"Generated {len(output_lines)} formatted lines.")
    return '\n'.join(output_lines) #return the batches on separate lines

#Example
#query_seq:
qs= "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTAGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAAACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCAAAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAG"

print(genbank_format(qs))
