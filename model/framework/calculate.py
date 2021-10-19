import csv
import sys, os

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)

from npscorer import readNPModel, scoreMolWConfidence
from rdkit import Chem

fscore = readNPModel()

infile = sys.argv[1]
outfile = sys.argv[2]

mols = []
with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        mols += [Chem.MolFromSmiles(r[0])]

R = []
for mol in mols:
    vals = scoreMolWConfidence(mol, fscore)
    R += [[vals.nplikeness, vals.confidence]]

with open(outfile, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["nplikeness", "confidence"])
    for r in R:
        writer.writerow(r)
