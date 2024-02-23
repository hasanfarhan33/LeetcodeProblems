'''
Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a function which translates a given DNA string into RNA.
'''

def dna_to_rna(dna): 
    characters = list(dna) 
    for i, char in enumerate(characters): 
        if characters[i] == "T": 
            characters[i] = "U"
    dna = "".join(characters)
    return dna

print(dna_to_rna("GCAT"))