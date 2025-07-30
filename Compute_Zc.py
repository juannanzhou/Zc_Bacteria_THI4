#!/usr/bin/env python3

import argparse
from Bio import SeqIO
import pandas as pd

# Mean carbon oxidation by amino acids
Pox = {
    'A': 0.00, 'C': 0.66, 'D': 1.00, 'E': 0.40, 'F': -0.44,
    'G': 1.00, 'H': 0.66, 'I': -1.00, 'K': -0.66, 'L': -1.00,
    'M': -0.40, 'N': 1.00, 'P': -0.40, 'Q': 0.40, 'R': 0.33,
    'S': 0.66, 'T': 0.00, 'V': -0.80, 'W': -0.18, 'Y': -0.22
}
# Carbon atom counts by amino acids
Cox = {
    'A': 3.00, 'C': 3.00, 'D': 4.00, 'E': 5.00, 'F': 9.00,
    'G': 2.00, 'H': 6.00, 'I': 6.00, 'K': 6.00, 'L': 6.00,
    'M': 5.00, 'N': 4.00, 'P': 5.00, 'Q': 5.00, 'R': 6.00,
    'S': 3.00, 'T': 4.00, 'V': 5.00, 'W': 11.00, 'Y': 9.00
}

# Calculate Zc score
def findox(sequence):
    totalsum = 0.0
    totalccount = 0.0
    aa_counts = {}
    for aa in sequence:
        if aa in Pox and aa in Cox:
            totalsum += Cox[aa] * Pox[aa]
            totalccount += Cox[aa]
        aa_counts[aa] = aa_counts.get(aa, 0) + 1
    freq = {aa: count / len(sequence) for aa, count in aa_counts.items()}
    Zc = totalsum / totalccount if totalccount else float('nan')
    return Zc, freq

def main():
    parser = argparse.ArgumentParser(
        description="Compute Zc values from a FASTA file and save as CSV"
    )
    parser.add_argument("input_file", help="Input FASTA file")
    parser.add_argument("output_file", help="Output CSV file path")
    args = parser.parse_args()  # :contentReference[oaicite:0]{index=0}

    ids = []
    Zc_list = []
    for record in SeqIO.parse(args.input_file, "fasta"):
        ids.append(record.id)
        seq = str(record.seq)
        try:
            zc, _ = findox(seq)
        except Exception:
            zc = float('nan')
        Zc_list.append(zc)

    df = pd.DataFrame({'GenBank': ids, 'Zc': Zc_list})
    df.to_csv(args.output_file, index=False)
    print(f"Wrote output to {args.output_file}")

if __name__ == "__main__":
    main()
