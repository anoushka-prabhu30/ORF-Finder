# ORF Finder - Final Combined Program
# Group Project - PCC

# Author: Anoushka Prabhu (Input Parsing)
# Author: Ashwarya Sharma (ORF Detection)
# Author: Pratham Patel (Output Formatting)

# PART 1: INPUT PARSING 

# Author: Anoushka Prabhu
def get_input():
    """Gets user input for FASTA filename."""
    f = input("Enter FASTA file: ")
    return f

# Author: Anoushka Prabhu
def parse(f):
    """Parses FASTA file and returns list of (header, DNA sequence)."""
    try:
        with open(f, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{f}' not found.")
        return []
    
    seqs = []
    i = 0
    
    while i < len(lines):
        # Check for header line starting with '>'
        if lines[i].startswith('>'): 
            h = lines[i].strip()[1:]
            i += 1
            parts = []
            # Collect sequence lines until next header
            while i < len(lines) and not lines[i].startswith('>'): 
                line = lines[i].strip().upper()
                # Remove whitespace and convert to uppercase
                line = ''.join(line.split()) 
                if line:
                    parts.append(line)
                i += 1
            dna = ''.join(parts)
            seqs.append((h, dna))
        else:
            i += 1
    
    return seqs

# Author: Anoushka Prabhu
def get_sequences():
    """Retrieves sequences from file."""
    f = get_input()
    seqs = parse(f)
    if not seqs:
        return []
    return seqs


# PART 2: ORF DETECTION 

# Author: Ashwarya Sharma
def reverse_complement(dna):
    '''Creation of the reverse complement of the given DNA sequence.'''
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    # Reverse the DNA sequence
    reverse = dna[::-1] 

    result = ''
    # Build complement strand base by base
    for letter in reverse: 
        if letter in complement:
            result = result + complement[letter]
        else:
            result = result + letter
    
    return result

# Author: Ashwarya Sharma
def orf_frame(dna, start_position, frame_number, original_length):
    '''Finds all ORFs in a specific reading frame using DNA sequence string, 
       starting position, and frame identifier.''' 
    orfs = []
    position = start_position
    
    while position <= len(dna) - 3:
        codon = dna[position:position+3]
        
        # Check for start codon
        if codon == 'ATG': 
            start = position
            new_position = position + 3
            
            found_stop = False
            # Looks forward in same frame for stop codon
            while new_position <= len(dna) - 3: 
                stop_codon = dna[new_position:new_position+3]
                
                # Stop codon found, then extract ORF
                if stop_codon == 'TGA' or stop_codon == 'TAG' or stop_codon == 'TAA': 
                    orf_sequence = dna[start:new_position+3]
                    orf_length = len(orf_sequence)
                    
                    if frame_number <= 3:
                        pos = start + 1
                    else:
                        # Calculate distance from right end for reverse strand
                        pos = -(original_length - start)
                    
                    orfs.append((frame_number, pos, orf_length, orf_sequence))
                    # Move to the end of this ORF to avoid smaller ORFs inside
                    position = new_position + 3 
                    found_stop = True
                    break
                
                new_position = new_position + 3
            
            if not found_stop:
                position = position + 3
        else:
            position = position + 3
    
    return orfs

# Author: Ashwarya Sharma
def find_orfs(dna):
    '''Finds all ORFs from 3 forward and 3 reverse sequences.'''

    all_orfs = []
    
    # Process forward strand (frames 1-3)
    for frame in range(3): 
        all_orfs.extend(orf_frame(dna, frame, frame + 1, len(dna)))

    # Process reverse complement strand (frames 4-6)
    rev_comp = reverse_complement(dna) 
    for frame in range(3):
        all_orfs.extend(orf_frame(rev_comp, frame, frame + 4, len(dna)))
    
    return all_orfs

# Author: Ashwarya Sharma
def filter_orfs(orfs, min_length):
    '''Filters ORFs by minimum length in base pairs'''
   
    f = []
    for orf in orfs:
        if orf[2] >= min_length:
            f.append(orf)
    return f


# PART 3: OUTPUT FORMATTING 

# Author: Pratham Patel
def format_codons(dna):
    """Formats DNA sequence into codons (15 per line)."""
    # Remove incomplete codon at the end if present
    if len(dna) % 3 != 0:
        dna = dna[:-(len(dna) % 3)]
    
    # Split sequence into codons (groups of 3 bases)
    codons = [dna[i:i+3] for i in range(0, len(dna), 3)]
    
    lines = []
    # Group codons into lines of maximum 15 codons
    for i in range(0, len(codons), 15): 
        lines.append(' '.join(codons[i:i+15])) 
    
    return '\n'.join(lines)

# Author: Pratham Patel
def print_orf(header, frame, pos, length, seq, output_file=None):
    """Prints a single ORF in FASTA format to screen or file."""
    line = f">{header} | FRAME = {frame} POS = {pos} LEN = {length}\n"
    line += format_codons(seq) + "\n\n"
    
    if output_file:
        output_file.write(line)
    else:
        print(line, end="")

# Author: Pratham Patel
def print_all_orfs(header, orfs, output_file=None):
    """Prints all ORFs for a given sequence to screen or file."""
    if not orfs:
        return
    for frame, pos, length, seq in orfs:
        print_orf(header, frame, pos, length, seq, output_file)


# MAIN PROGRAM

# Author: Anoushka Prabhu, Ashwarya Sharma, Pratham Patel
def main():
    # Get sequences from input file
    sequences = get_sequences() 
    
    if not sequences:
        return

    # Ask user for minimum ORF length (default = 50)
    m = input("Enter minimum length in bp for ORFs (default=50): ") 

    try:
        min_length = 50 if m.strip() == "" else int(m)
    except ValueError:
        print("Invalid input. Using default = 50.")
        min_length = 50
    
    # Ask user if they want to save output to a file
    save_option = input("Save output to file? (y/n): ").lower().strip()
    output_file = None
    
    if save_option == 'y':
        filename = input("Enter output filename (default: orfs_output.txt): ").strip()
        if filename == "":
            filename = "orfs_output.txt"
        output_file = open(filename, 'w')
        print(f"\nSaving results to {filename}...\n")
    
    # Process each sequence
    for header, dna in sequences:
        orfs = find_orfs(dna)
        orfs = filter_orfs(orfs, min_length)
        
        if orfs:
            # Sort ORFs by frame and position before printing
            orfs.sort(key=lambda x: (x[0], x[1])) 
            print_all_orfs(header, orfs, output_file)
        else:
            msg = f">{header} | No ORFs found\n\n"
            if output_file:
                output_file.write(msg)
            else:
                print(msg, end="")
    
    # Close file if it was opened
    if output_file:
        output_file.close()
        print(f"\nResults saved to {filename}")

if __name__ == "__main__":
    main()
