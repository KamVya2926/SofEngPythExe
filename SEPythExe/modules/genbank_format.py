"""
This function is called genbank_format. It does the following:
1. Takes a string (query_seq) and a chunk size (chunk_size), which is set at 10 characters.
2.Breaks the string into chunks of chunk_size.
3. Prints the output in the format of GenBank DNA sequence entries. So,
    6 chunks per line (ignoring everything apart from letters, and always in lower case - line 12)
    with each line prefixed with the number of the first character in the line
    based on its order in the original string.

"""
def genbank_format(query_seq, chunk_size= 10):
    query_seq = ''.join([char for char in query_seq if char.isalpha()]).lower()
    chunks = [] #initialise an empty list to store the chunks

#Nested for loop
#First loop going through query_seq in steps set by chunk_size to extract substrings of same size
#Substrings will be appended to chunks list
#Output will be all substrings in one line
    for i in range(0, len(query_seq), chunk_size):
        chunks.append(query_seq[i:i+chunk_size])


#Second for loop going thorough substrings in chunks list
#Starts from 0 going up to number of substrings set by len(chunks) in batches of 6
#Prints batches on separate lines with substrings seperated by a space
#(f"{start_index:>3}:" prints index of the first character in the line right-aligned followed by a colon

    for i in range(0, len(chunks), 6):
        start_index = i * chunk_size+ 1  # Index of the first character in this line, starting at 1
        line_chunks = chunks[i:i + 6] #Batch of substrings assigned to variable
        print(f"{start_index:>3}:", ' '.join(line_chunks))


#Example
#query_seq:
qs= "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTAGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAAACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCAAAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAG"

print(genbank_format(qs))