# Import the regular expressions module
import re
# Open input file containing DNA sequences
data = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
# Prompt user to enter a stop codon
print("Please enter a stop codon [TAA/TAG/TGA]")
stop_codons = input("")
# Check if the input is a valid stop codon using regex
if not re.match("TAA|TAG|TGA", stop_codons):
    print("The input is not a stop codon")
else:
    # Open output file for genes with the specified stop codon
    output = open(stop_codons+"_stop_genes.fa", "w")
    # Initialize an empty string to store the DNA sequence
    seq = ""
    # Loop through each line of the input file
    for line in data:
        # Check if the line starts with ">", indicating a new gene sequence
        if line.startswith(">"):
            # Add a newline character to the sequence string
            seq += "\n"
            # Extract the gene ID from the line using regex
            gene = re.split(" ", line, 1)[0]
            # Check if the current sequence contains the specified stop codon
            if re.findall(stop_codons, seq):
                # If so, count the number of occurrences of the stop codon in the sequence
                num = len(re.findall(stop_codons, seq))
                # Write the gene ID and number of stop codons to the output file
                output.write(seq%(str(num)))
            # Reset the sequence string for the new gene
            seq = ""
            # Reset the count of lines in the sequence to zero
            count = 0
            # Reset the count of stop codons to zero
            num = 0
        # If the line does not start with ">", it contains DNA sequence data
        elif not line.startswith(">"):
            # Increment the count of lines in the sequence by 1
            count += 1
            # If this is the first line of sequence data, add the gene ID and a placeholder for the number of stop codons to the sequence string
            if count == 1:
                seq += gene + " coding_sequences: %s" + "\n"
            # Add the sequence data to the sequence string, removing the newline character at the end of the line
            seq += line[:-1]
# Close the input and output files
data.close()
output.close()