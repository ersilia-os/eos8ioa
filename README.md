# Natural product score

## Model Identifiers
- Slug: natural-product-score
- Ersilia ID: eos8ioa
- Tags: fingerprint,	drug-likeness,	NP

Model Description 
A simple score to distinguish between natural product (-like) and synthetic compounds 
- Input: SMILES 
- Output: Score 
- Model type: Regression
- Mode of training: Pretrained
- Training data: 290,000 compounds 
- Experimentally validated: No 

## Source code
This model is published by Peter Ertl, Silvia Roggo, & Ansgar Schuffenhauer. Natural Product-likeness Score and Its Application for Prioritization of Compound Libraries. *Journal of Chemical Information and Modeling*, 48(1), 68–74. DOI: [10.1021/ci700286x](https://pubs.acs.org/doi/abs/10.1021/ci700286x) (2008).
- Code: https://github.com/rdkit/rdkit/tree/master/Contrib/NP_Score
- Checkpoints: https://github.com/rdkit/rdkit/blob/master/Contrib/NP_Score/publicnp.model.gz

## License
The GPL-v3 license applies to all parts of the repository that are not externally maintained libraries. This repository uses the externally maintained library "NP_Score", located at `/model` and licensed under a BSD-3 License

## History 
- Model was downloaded and incorporated on October 19, 2021
