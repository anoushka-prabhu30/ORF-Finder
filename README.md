# PCC Final Group Project: ORF Finder

## Project Overview

This project implements a Python program that finds all Open Reading Frames (ORFs) in DNA sequences from a FASTA file. An ORF is a sequence of DNA that starts with a start codon (ATG) and ends with a stop codon (TAA, TAG, or TGA). The program analyzes all 6 reading frames (3 forward frames and 3 reverse complement frames) and outputs ORFs that meet a user-specified minimum length.

## How the Program Works
User Input (FASTA file + min length)
↓
Parse FASTA file
↓
For each DNA sequence:
Analyze 6 frames
Find all ORFs (start → stop)
Filter by minimum length
↓
Output ORFs in FASTA format
(headers with frame, position, length)
(codons grouped, 15 per line)


## Team Collaboration

Our team divided the project into three main modules, each assigned to one team member. This allowed parallel development and clear ownership of specific functionality.

### Task Distribution

| Team Member | Module | Responsibility |
|-------------|--------|----------------|
| Anoushka Prabhu | Input Parsing | Read FASTA file, handle user input, return sequences |
| Ashwarya Sharma | ORF Detection | Find start/stop codons in all 6 frames, calculate positions |
| Pratham Patel | Output Formatting | Print results in FASTA format with proper codon grouping |

All communication and code sharing was done through Canvas discussions and a shared GitHub repository.

## Individual Contributions

### Anoushka Prabhu - Input Parsing Module

**File:** `input_parser.py`

**Functions implemented:**
- `get_input()` - Prompts user for FASTA filename and minimum ORF length (default = 50)
- `parse(f)` - Reads and parses FASTA file, handles multiple sequences, ignores whitespace, converts to uppercase
- `get()` - Main interface function that returns sequences and minimum length

**Key features:**
- Handles any number of sequences per file
- Sequences may be split over many lines
- Case-insensitive (converts everything to uppercase)
- Ignores whitespace in sequence data
- Error handling for missing files

**Output format from this module:**
```python
sequences = [("header1", "ATGC..."), ("header2", "ATGC...")]
min_length = 50
```
Integration

Obstacles Faced
Understanding reverse complement coordinates - Calculating negative positions for frames 4-6 was challenging. We resolved this by carefully testing with sample sequences and verifying against provided output.

Handling multiple sequences in one file - Ensuring the parser correctly separates sequences and the ORF finder processes each independently required careful loop logic.

Codon formatting with proper line breaks - Implementing the 15-codon per line limit while maintaining correct spacing required careful string manipulation.

Coordinate synchronization between modules - Ensuring Ashwarya's position calculation matched Pratham's header formatting needed clear communication and agreed-upon data structures.

Future Improvements
Support for ambiguous nucleotides - Currently only handles A, T, G, C. Could extend to handle N and other IUPAC codes.

Multiple start codons - Some organisms use alternative start codons (GTG, TTG). Could add configuration options.

Report generation - Could generate summary statistics (total ORFs, length distribution, frame distribution).

Graphical user interface - Add file browser and visual sequence viewer.

Output to file - Add option to save results to a file instead of only printing to console.

Performance optimization - For very long sequences, optimize the ORF scanning algorithm.

Conclusion
The ORF Finder program successfully identifies all open reading frames in DNA sequences across all 6 reading frames. The modular design allowed three team members to work in parallel on distinct components (input parsing, ORF detection, output formatting). The program meets all specifications: accepts FASTA input with multiple sequences, handles user-specified minimum ORF length, outputs in correct FASTA format with frame number, position, length, and properly formatted codons (15 per line with spaces).

Submitted as partial fulfillment of PCC Group Project requirements.
