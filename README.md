# OTU_predictor

`OTU_predictor` uses a trained `RandomForestClassifier` ML model to predict 'real' OTU presence from ancient metagenomic samples (although it's use is not limited to ancient samples). The training dataset consists of 200 simulated populations generated through [InSilicoSeq](https://github.com/HadrienG/InSilicoSeq) and deaminated using [gargammel](https://github.com/grenaud/gargammel). Each population contains between 5 and 20 microbial species with know, variable abundance. `OTU_predictor` uses input files generated in [centrifgure](https://ccb.jhu.edu/software/centrifuge/), specifically `centrifugeReport.txt` files.

## Install package

The easiest way to install `OTU_predictor` is using `pip`. The following command will do this:

```bash
pip install git+https://github.com/DrATedder/OTU_predictor.git
```
