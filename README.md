# Natural product score

A simple score to distinguish between natural products (-like) and synthetic compounds. The score was calculated using an analysis of the structural features that distinguish natural products (NP) from synthetic molecules. NP structures were obtained from the CRC Dictionary of Natural products and synthetic molecules belong to an in-house collection. This method has been contributed to the RDKit package, Ersilia is simply implementing the RDKit NP\_Score.

This model was incorporated on 2021-10-19.

## Information
### Identifiers
- **Ersilia Identifier:** `eos8ioa`
- **Slug:** `natural-product-score`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Natural product`, `Drug-likeness`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Higher score indicates higher natural product likeness

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| nplikeness | float | high | Natural product likeness score |
| confidence | float | high | Confidence of the natural product likeness score |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos8ioa](https://hub.docker.com/r/ersiliaos/eos8ioa)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8ioa.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8ioa.zip)

### Resource Consumption
- **Model Size (Mb):** `5`
- **Environment Size (Mb):** `440`
- **Image Size (Mb):** `400.32`


### References
- **Source Code**: [https://github.com/rdkit/rdkit/tree/master/Contrib/NP_Score](https://github.com/rdkit/rdkit/tree/master/Contrib/NP_Score)
- **Publication**: [http://pubs.acs.org/doi/abs/10.1021/ci700286x](http://pubs.acs.org/doi/abs/10.1021/ci700286x)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2007`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [BSD-3-Clause](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos8ioa
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos8ioa
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
