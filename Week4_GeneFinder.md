# Week 4 

# Step 1. 

## Install Biopython 
pip install biopython  
> Successfully installed biopython-1.84 numpy-2.0.2

# Step 2. 

## Initialize git repository 
mkdir Week_4  
cd Week_4  
git init  
touch Gene_finder.py README.md

# Question 1. 
### Extracting ORFs from a FASTA file
 nano Gene_finder.py  
 git add Gene_finder.py README.md  
 git commit -m "added Gene_finder.py"  
 > python Gene_finder.py example1.fasta
 
# Question 2. 
### Extracting ORFs from a fasta file including reverse complement
nano Gene_finder_reverse.py  
git add Gene_finder_reverse.py  
git commit -m "added Gene_finder_reverse.py"  
> python Gene_finder_reverse.py example1.fasta

# Question 3. 
### Open Reading Frame problem on Rosalind (Problem 72)

# Question 4. 
### Find all Open Reading Frames in the 14 genomes you downloaded

