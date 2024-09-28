# BIO-InformaticaProject

# PROBLEM 2
## Copy the files to your home directory on IBEX. Uncompress the zip file on IBEX.
scp C:\Users\CHUYASCM\Desktop\Bioinformatic\Assigment2_Week2\BacterialGenome_dataset.zip  chuyascm@ilogin.ibex.kaust.edu.sa:~/

OUTPUT:
BacterialGenome_dataset.zip                                                           100%   16MB   7.1MB/s   00:02

# PROBLEM 3

## The largest genome 
find /home/chuyascm/ncbi_dataset/data -name "*.fna" -exec sh -c 'echo "$(tail -n +2 "$1" | wc -c) $(basename "$1")"' _ {} \; | sort -n | tail -n 1 | awk '{print "The largest genome is in \"" $2 "\": " $1}'

OUTPUT: The largest genome is in "GCF_000006745.1_ASM674v1_genomic.fna": 4083974
