data directory
==============

Storing genomic data in git repos is generally a bad idea. The exception is
demonstration or test data (the files here fall under these categories).

## E. coli ##

Escherichia coli strain K-12 standard files from NCBI downloaded 2022-12-19.

- `GCF_000005845.2_ASM584v2_genomic.fna.gz` fasta file of genome
- `GCF_000005845.2_ASM584v2_genomic.gbff.gz` GenBank flat file
- `GCF_000005845.2_ASM584v2_genomic.gff.gz` GFF file
- `GCF_000005845.2_ASM584v2_protein.faa.gz` fasta file of proteins

## Model Organisms ##

Sequence (fasta) and annotation (gff) files are provided for 3 famous model
organisms. The first 1 percent of each chromosome is represented in FASTA and
GFF formats. The C.elegans genome also has a file of transcript sequences and
variant information.

- A. thaliana
- C. elegans
- D. melanogaster

## Other Files ##

- `colors_basic.tsv` 15 HTML color names
- `colors_extended.tsv` 440 HTML color names
- `dictionary.gz` a list of 109,421 unique English words
- `jaspar2024_core.transfac.gz` the JASPAR database of transcription sites
