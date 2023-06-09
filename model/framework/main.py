# imports
import os
import csv
import sys
from rdkit import Chem

from npscorer import readNPModel, scoreMolWConfidence


fscore = readNPModel()


ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)



# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# my model
def my_model(smiles_list):
    R = []
    for smi in smiles_list:
        mol=Chem.MolFromSmiles(smi)
        vals = scoreMolWConfidence(mol, fscore)
        R.append([vals.nplikeness, vals.confidence])
    return R
    


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = my_model(smiles_list)

print(outputs)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["nplikeness", "confidence"])
    for r in outputs:
        writer.writerow(r)




