import argparse
from Bio import SeqIO
from Bio.Seq import Seq

def find_ORF(sequence):
    ORFs = []
    n = len(sequence)

    for frame in range(3):
        for start in range(frame, n, 3):
            codon = sequence[start:start+3]
            if codon == 'ATG':
                for end in range(start + 3, n, 3):
                    stop_codon = sequence[end:end+3]
                    if stop_codon in ['TAA', 'TAG', 'TGA']:
                        ORF = sequence[start:end+3]
                        ORFs.append((start, end+3, ORF))
                        break
    return ORFs

def main(input_file):
    for record in SeqIO.parse(input_file, "fasta"):
        sequence = str(record.seq)
        ORFs = find_ORF(sequence)

        for start, end, orf in ORFs:
            print(f">ORF_{start}_{end}")
            print(orf)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find ORFs in a FASTA file")
    parser.add_argument("input_file", help="Input FASTA file")
    args = parser.parse_args()

    main(args.input_file)
