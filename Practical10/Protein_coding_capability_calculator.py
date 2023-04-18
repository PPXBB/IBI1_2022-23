def calculator(seq):
    """Determines if a DNA sequence is protein-coding or not based on the
    percentage of sequence between start and stop codons."""
    # Convert to upper case
    data = seq.upper()
    # Find start and stop codon positions
    start = data.find("ATG")
    stop = data.find("TGA")
    total = len(data)
    coding = stop - start
    coding_percentage = (coding/total) * 100
    # Determine if protein-coding, non-coding or unclear
    if coding_percentage > 50:
        label = "protein-coding"
    elif coding_percentage < 10:
        label = "non-coding"
    else:
        label = "unclear"
    return coding_percentage ,label

# Example function call
dna = "accatggccatgcccagctgcatgcatcatga"
result = calculator(dna)
print(result)