# Natural product score

A simple score to distinguish between natural products (-like) and synthetic compounds. The score was calculated using an analysis of the structural features that distinguish natural products (NP) from synthetic molecules. NP structures were obtained from the CRC Dictionary of Natural products and synthetic molecules belong to an in-house collection. This method has been contributed to the RDKit package, Ersilia is simply implementing the RDKit NP\_Score.

## Identifiers

* EOS model ID: `eos8ioa`
* Slug: `natural-product-score`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Regression`
* Output: `Score`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Higher score indicates higher natural product likeness

## References

* [Publication](http://pubs.acs.org/doi/abs/10.1021/ci700286x)
* [Source Code](https://github.com/rdkit/rdkit/tree/master/Contrib/NP_Score)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos8ioa)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8ioa.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos8ioa) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](http://pubs.acs.org/doi/abs/10.1021/ci700286x) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a BSD-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!