# Open and read the BLOSUM62 matrix file
BLOSUM62 = open("BLOSUM62.txt")
BLOSUM62_matrix = BLOSUM62.readlines()[6:]
BLOSUM62_matrix = [line.rstrip() for line in BLOSUM62_matrix]
# Initialize the dictionary
blosum62 = {}
# Extract the keys and values
for i in range(1, len(BLOSUM62_matrix)):
    BLOSUM62_matrix[i] = BLOSUM62_matrix[i].split()[1:]
keys = BLOSUM62_matrix[0].replace(" ","")
values = BLOSUM62_matrix[1:]
# Construct the dictionary
for i in range(0, len(keys)):
    for j in range(0, len(keys)):
        blosum62[(keys[i], keys[j])] = int(values[i][j])
# Open the fasta files for cat, mouse and human ACE2 sequences
cat = open("ACE2_cat.fa")
mouse = open("ACE2_mouse.fa")
human = open("ACE2_human.fa")
# Read the sequences from the files
cat_seq = cat.readlines()
mouse_seq = mouse.readlines()
human_seq = human.readlines()

def global_align (seq1, seq2):
    """ Perform global alignment between two sequences seq1 and seq2. """
    Seq1_name = seq1[0]
    Seq1 = seq1[1].rstrip()
    Seq2_name = seq2[0]
    Seq2 = seq2[1].rstrip()
    score = 0
    same = 0
    compair = list(zip(Seq1, Seq2))
    for pair in compair:
        if pair[0]==pair[1]:
            same += 1
        score += blosum62[pair]
    per = same/len(Seq1)*100
    # Print the alignment results
    print("Seq: ")
    print(Seq1_name+Seq2_name, end = "")
    print("Alignment Matrix: BLOSUM62")
    print("Alignment Score:", score)
    print("Identical Percentage:", per)
    print()
    return score

# Call the global_align function to get the scores for the three alignments
hc_score = global_align(cat_seq, human_seq)
hm_score = global_align(human_seq, mouse_seq)
cm_score = global_align(cat_seq, mouse_seq)
cat.close()
mouse.close()
human.close()