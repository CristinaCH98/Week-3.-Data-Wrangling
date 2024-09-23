# BIO-InformaticaProject

# PROBLEM 2
# (1 point) Copy the files to your home directory on IBEX. Uncompress the zip file on IBEX.
scp C:\Users\CHUYASCM\Desktop\Bioinformatic\Assigment2_Week2\BacterialGenome_dataset.zip  chuyascm@ilogin.ibex.kaust.edu.sa:~/

OUTPUT:
BacterialGenome_dataset.zip                                                           100%   16MB   7.1MB/s   00:02

# PROBLEM 3

# The largest genome 
find /home/chuyascm/ncbi_dataset/data -name "*.fna" -exec sh -c 'echo "$(tail -n +2 "$1" | wc -c) $(basename "$1")"' _ {} \; | sort -n | tail -n 1 | awk '{print "The largest genome is in \"" $2 "\": " $1}'

OUTPUT: The largest genome is in "GCF_000006745.1_ASM674v1_genomic.fna": 4083974

# The smallest genome 

find /home/chuyascm/ncbi_dataset/data -type f -name "*.fna" -exec sh -c 'echo "$(tail -n +2 "$1" | wc -c) $(basename "$1")"' _ {} \; | sort -n | head -n 1 | awk '{print "The smallest genome is in \"" $2 "\": " $1}'

OUTPUT: The smallest genome is in "GCA_000008725.1_ASM872v1_genomic.fna": 1055551

# PROBLEM 4

# 4.1 Find the number of genomes that contain at least two “c” in the species name. 

find /home/chuyascm/ncbi_dataset/data -type f -name "*.fna" -exec sh -c 'grep -E "^>" "$1" | awk -F " " "{print \$2}" | grep -E "c.*c" | wc -l' _ {} \; | awk '{total += $1} END {print total}'

OUTPUT: 14

# 4.2 How many of the species names contain two or more “c” but do not contain the word “coccus”?

find /home/chuyascm/ncbi_dataset/data -type f -name "*.fna" -exec sh -c 'grep -E "^>" "$1" | awk -F " " "{print \$2}" | grep -E "c.*c" | grep -v "coccus" | wc -l' _ {} \; | awk '{total += $1} END {print total}'

OUTPUT: 4 

# PROBLEM 5

# Use the find command to find all genome files (FASTA) larger than 3 megabyte. 

find /home/chuyascm/ncbi_dataset/data -type f -name "*.fna" -size +3M | wc -l

OUTPUT: 6 


