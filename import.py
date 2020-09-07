"""
This is the script that imports the global proteomic data into Graphpad Prism. I have manually collated the proteins that are statistically signficant according to the two-sample t test in (i) Vehicle Ipsilateral vs Fasudil Ipsilateral (ii) Vehicle Contralateral vs Fasudil Contralateral. The script identifies the M/L ratios across the 4 samples for each protein in the list and generates a table that is ready to be imported into Prism
"""

import sys

filename = sys.argv[1]

with open('List of Genes.txt', 'rt') as f:
    genes = set(f.readlines())


with open(filename, 'rt') as f:
    rows = f.readlines()

for row in rows:
    row = row.split(',')
    if row[0] in genes:
        with open(row[0] + '.txt', 'wt') as f:
            f.write("\t" + "Contralateral\t" * 4 + "Ipsilateral\t" * 4 + "\n")
            f.write("Vehicle\t" + "\t".join(row[10:17]) + "\n")
            f.write("Fasudil\t" + "\t".join(row[2:9]) + "\n")
