# Importing the regular expression module
import re
# Defining a DNA sequence
seq = "ATGCAATCGACTACGATCTGAGAGGGCCTAA"
# Split the sequence at the first occurrence of the start codon "ATG"
start_codon = re.split("ATG", seq, 1)
# Initializing a variable to keep track of the number of possible stop codons
possible_number = 0
# Check if a start codon was found in the sequence
if len(start_codon) > 1:
    # Using regular expressions to find all occurrences of "TAA", "TAG", or "TGA" in the substring following the start codon
    coding = re.findall(r"(TAA|TAG|TGA)", start_codon[1])
    # Counting the number of possible stop codons found
    possible_number = len(coding)
# Printing the number of possible stop codons
print(possible_number)