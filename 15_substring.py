# Find a repeated substring in a given strng

def rep_char(dna, x):
    dict = {}
    for i in range(0, len(dna)):
        sub_str = dna[i:i + x]
        if sub_str in dict:
            dict[sub_str] += 1
        else:
            dict[sub_str] = 1

    for k, v in dict.items():
        if v > 1:
            print k+":", v,


dna = "aaaacccaaagggtttaaacccgggtttgc"

rep_char(dna, 5)
