# PCC Final Group Project: ORF Finder

## Project Overview

This project implements a Python program that finds all **Open Reading Frames (ORFs)** in DNA sequences from a FASTA file. An ORF is a sequence of DNA that begins with a start codon (`ATG`) and ends with a stop codon (`TAA`, `TAG`, or `TGA`). The program analyzes all **6 reading frames** (3 forward + 3 reverse complement) and outputs ORFs that meet a user-specified minimum length.

---

## How the Program Works

```
User Input (FASTA file + min length + optional output file)
            │
            ▼
    Parse FASTA file
            │
            ▼
  For each DNA sequence:
    ├── Analyze 6 reading frames
    ├── Find all ORFs (start codon → stop codon)
    └── Filter by minimum length
            │
            ▼
  Output ORFs in FASTA format
    ├── Header: frame, position, length
    └── Sequence: codons grouped, 15 per line
            │
            ▼
    Screen display OR save to file
```

---

## How to Run the Program

### Method 1: Using IDLE

1. Open `orfs.py` in IDLE
2. Press **F5** or go to **Run → Run Module**
3. Follow the prompts:
   - Enter the FASTA file name (e.g., `sequence.fasta`)
   - Enter the minimum ORF length in bp (press **Enter** for default: `50`)
   - Enter `y` to save output to a file, or `n` to display on screen only
4. If saving, results will be written to your chosen output filename

### Method 2: Using the Command Line

```bash
python orfs.py
```

---

## Sample Run

```
Enter FASTA file: sequence.fasta
Enter minimum length in bp for ORFs (default=50): 300
Save output to file? (y/n): y
Enter output filename (default: orfs_output.txt):
Saving results to orfs_output.txt...
Results saved to orfs_output.txt
```

---

## Output Format

ORFs are written in FASTA format with a descriptive header line, followed by the sequence grouped into codons (15 codons per line):

```
>Test1 | FRAME = 1  POS = 25  LEN = 996
ATG GCT CCC AAG GGT TTA ATC TTT TTG GCT GTG TTA TGC TTC TCA
GCA CTG TCA CTG AGT CGT TGT CTT GCG GAG GAT AAT GGA CTT GTT
TGA

>Test1 | FRAME = 6  POS = -933  LEN = 324
ATG GCA CCA AAC TTG TCA AGA ACT GCA GAA ATG GAT TCA TTG TGG
TCT GGG AGG AAC TGC TCT ACC ACA TCG GCT CTG CTC CTT CTA CCA
CAA CTC TGA
```

**Header fields:**
- `FRAME` — reading frame (1–3 for forward strand, 4–6 for reverse complement)
- `POS` — start position in the original sequence (negative values indicate reverse strand)
- `LEN` — length of the ORF in base pairs

---

## Key Features

- Handles **multiple sequences** per FASTA file
- **Case-insensitive** — all input is converted to uppercase
- **Ignores whitespace** in sequence data
- Scans all **6 reading frames** (3 forward, 3 reverse complement)
- Filters ORFs by a **user-specified minimum length**
- Outputs to **screen** or saves to a **file**
- Sequences formatted as **space-separated codons**, 15 per line
- **Error handling** for missing or invalid input files

---

## Team Collaboration

Our team divided the project into three main modules:

| Team Member     | Module            | Responsibility                                                            |
|-----------------|-------------------|---------------------------------------------------------------------------|
| Anoushka Prabhu | Input Parsing     | Read FASTA file, handle user input, return sequences                      |
| Ashwarya Sharma | ORF Detection     | Find start/stop codons in all 6 frames, calculate positions               |
| Pratham Patel   | Output Formatting | Print results in FASTA format with proper codon grouping                  |

All communication and code sharing was done through Canvas discussions and in-person meetings.

---

## Requirements

- Python 3.x
- No external libraries required — uses the Python standard library only

---

## Files Included

| File              | Description                  |
|-------------------|------------------------------|
| `orfs.py`         | Main program                 |
| `sequence.fasta`  | Sample input FASTA file      |
| `README.md`       | Project documentation        |
