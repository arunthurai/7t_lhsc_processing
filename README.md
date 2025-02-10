# 7T LHSC Clinical Data Processing Pipeline 
AIMS Lab Research Team at the Robarts Research Institute - 2024-2025

*This package is under active development. It should be stable and reproducible, but please let any of the active contributing members know if there are any bugs or unusual behaviour.*

This Python package is a data processing pipeline based on Snakemake, utilizing the Snakebids format for some rules

## Brief Overview of the Pipeline
1. Converts CFMM data to tar file
2. Converts Tar to Bids formatting 
3. Utilizes gradcorrect
4. Utilizes prepdwi

## Table of Contents
1. [Installation](#installation)

## Installation

### Installing Poetry
We use poetry tool for dependency management and to package the python project. You can find step by step instructions on how to install it by visiting it's official [website](https://python-poetry.org/docs/).

### Local Installation

After installing poetry, clone this repository via:

```bash
git clone https://github.com/arunthurai/7t_lhsc_processing.git
```

You can then install the python package using one of the following commands, which should be executed within the repository folder (i.e., 7t_lhsc_processing/).

To install the 7t_lhsc_processing package "normally", use: 

```bash
poetry install 
```
```bash
poetry shell 
```

## Quick Guide
- currently only dry runs of the workflow have been tested

To execute a dry-run of the workflow, use:

```
clinical_processing_7t output_dir cfmm_id -np
```

To execute a wet-run of the workflow, use:

```
clinical_processing_7t output_dir cfmm_id --use-singularity
```

## Current changes in progress
- editing the wildcards to pull from file names instead of hard coding for testing
- testing the entire workflow as at wet run instead of dry runs 





