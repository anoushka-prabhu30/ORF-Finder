#Detecting ORFs

def determining_orfs:

    orfs = []
    i = start
    
    while i <= len(dna) - 3:
        codon = dna[i:i+3]
        
      
        if codon == 'ATG':
            start_codon = i
            ORF = i + 3
           
            while ORF <= len(dna) - 3:
                stop_codon = dna[ORF:ORF +3]
                
                if stop_codon == 'TGA' or stop_codon == 'TAG' or stop_codon == 'TAA':
                    orf = dna[start_codon:ORF+3]
                    
                    if len(orf) >= min_len:
                        pos = -(len(dna) - start_pos)
                        orfs.append((frame_num, pos, orf))
                    
                    i = ORF + 3  
                    break
                ORF += 3
        else:
            i += 3
    return orfs


filename = input("Enter filename: ")
min_len = int(input("Minimum ORF length (50): ")


header = ""
sequence = ""

with open(_______) as f:
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            if sequence:  
                orfs = find_orfs(sequence, min_len)
                for frame, pos, orf in orfs:
                    print_orf(header, frame, pos, orf)
                    print()
            header = line[1:]
            sequence = ""
        else:
            sequence += line.upper().replace(' ', '')

if sequence:
    orfs = find_orfs(sequence, min_len)
    for frame, pos, orf in orfs:
        print_orf(header, frame, pos, orf)
        print()
