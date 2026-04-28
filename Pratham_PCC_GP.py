#format and print output
#Author- Pratham Patel 

def format_sequence(d):
    codons = [d[i:i+3] for i in range(0, len(d)-2, 3)]
    lines = []

    for i in range(0, len(codons), 15):
        lines.append(' '.join(codons[i:i+15]))

    return '\n'.join(lines)

def print_orfs(h, orfs, d):

    for frame, start, length, seq in orfs:

        if frame <= 3:
            pos = start + 1
        else:
            pos = -(len(d) - start - 1)

        print(f">{h} | FRAME = {frame} POS = {pos} LEN = {length}")
        print(format_sequence(seq))
        print()
