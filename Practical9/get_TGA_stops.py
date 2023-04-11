# Import the regular expressions module
import re
# Open input file containing DNA sequences
data = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
# Create output file for TGA stops genes
output = open("TGA_genes.fa", "w")
# Initialize an empty string to store the DNA sequence
seq = ""
# Loop through each line of the input file
for line in data:
    # Check if the line starts with ">", indicating a new gene sequence
    if line.startswith(">"):
        # Extract the gene ID from the line using regex
        gene = re.split(" ", line, 1)[0]
        # Check if the previous sequence ends with "TGA", indicating a potential stop codon
        if re.search("TGA$", seq):
            # If so, write the sequence to the output file
            output.write(seq)
        # Reset the sequence string for the new gene
        seq = ""
        # Reset the count of lines in the sequence to zero
        count = 0
    # If the line does not start with ">", it contains DNA sequence data
    elif not line.startswith(">"):
        # Increment the count of lines in the sequence by 1
        count += 1
        # If this is the first line of sequence data, add the gene ID to the sequence string
        if count == 1:
            seq += gene + "\n"
        # Add the sequence data to the sequence string
        seq += line
# Close the input and output files
data.close()
output.close()