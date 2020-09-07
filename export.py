import glob
import re
import collections

exported = glob.glob("Analysis/*.txt")
genelist = []

for sheets in exported:
    name = re.search(r'(\w+)\.', sheets).group(1)
    with open(sheets, "rt") as f:
        data = f.readlines()

        for row in data:
            if "  Fasudil:Ipsilateral vs. Vehicle:Ipsilateral" in row or "  Fasudil:Contralateral vs. Vehicle:Contralateral" in row:
                test = row.replace('\t'*3,'').split('\t')
                comp = ''.join(re.findall(r'([A-Z])+', test[0]))
                if len(test) == 6:
                    genelist.append((name, comp, test[1], test[-1].replace('\r\n', ''), test[-2]))


genes = collections.defaultdict(list)

for name, comp, meandiff, pval, summ in genelist:
    genes[name].append((comp, meandiff, pval.strip(), summ))

with open('ANOVA_complete.tsv', 'wt') as f:
    f.write("Gene\tFCVC\tInterp\tStars\tFIVI\tInterp\tStars\n")
    for k,j in genes.items():
        h,i = j
        f.write("{}\t{}\t{} ({})\t{}\t{}\t{} ({})\t{}\n".format(k, h[0], h[1], h[2], h[3], i[0], i[1], i[2], i[3]))


