# Archaeo Structures
This project uses convolutional neural networks (CNNs) to autonomously detect archaeological features in satellite and historical aerial imagery. It leverages computer vision to dramatically upscale survey coverage compared to field-based survey methods. While field methods can cover 1-2 square kilometers a day, this form of CNN-aided virtual survey will enable tens or hundreds of thousands of square kilometers to be surveyed autonomously.  Systematic survey at this inter-regional scale promises to produce new insights into late prehistoric (~1000-1532 CE) and colonial-era (1532-1821 CE) settlement patterns, economic variation and change, and the effects of Spanish colonialism.

The project is situated in the western cordillera of the southern Peruvian Andes. This region is especially well-suited to survey from satellite imagery because the arid environment limits vegetation coverage that would otherwise obscure relevant features. The project focuses on archaeological sites with standing architectural remains visible in the imagery.  Relict buildings were primarily constructed from stone and therefore have maintained relatively good levels of preservation, making them readily visible in the imagery. However, because they are composed of the same materials as the background matrix (soil, rock), relict buildings are not spectrally distinct, making traditional remote sensing techniques ineffective. For this reason, we have trained a CNN to detect architectural features.

Currently, the project is using a slightly modified version of the [Raster Vision](https://github.com/azavea/raster-vision)  library for the processing of the satellite imagery into image chips to supply the machine learning algorithms. This can easily be expanded on though alternative solutions are welcome. The backend for Raster Vision is PyTorch.

## Project Goals
1. Build a model with at least 90% recall rate and 95% or more precision at identifying archeological structures.
2. Build a model to classify the results of the previous model into one of a selection of categories (Corral, Settlement, Isolated Structure, Mixed Modern,...)
3. Compare results with existing survey data (terrestrial and satellite based) to evaluate the usefulness of automated survey.
4. Establish methods to create future models for studying agricultural terracing and other features of archaeological interest

## Data Sources
- Imagery sources: ~4,000 square kilometers of Worldview I and Worldview II Satellite Imagery covering a portion of the western cordillera of the southern Peruvian Andes.
  - Worldview I (~3000 sqkm)
    - 8 spectral bands
    - 0.5 m resolution
  - Worldview II (~1000 sqkm)
    - 8 spectral bands
    - 0.3 m resolution
- Archaeological sources:
  - ~6,000 76x76 meter tiles, coded for presence/absence of archaeological structures
    - ~600 positives
    - ~5400 negatives
  - Previous archaeologcal survey data for portions of the region
  - Large scale manual satellite survey data overlapping much of the region (Collection ongoing, available summer of 2021)

### Data Location
Contact James (information below) to access the data.

## Project Timeline (Subject to refinement)
* February 2021
  * Refining current model
* March 2021
  * Adding classification functionality
* April 2021
  * Submission of paper detailing initial results
  * Model Refinement(s)
* Summer 2021
  * Comparison to existing survey data
  * Beginning agricultural terracing project


## Current Status
A preliminary model has shown promising results, With a recall rate of ~80% and a precision of ~80%. This has room to be improved, particularly with regards to distinguishing between modern and archaeological structures.

## Contact information
### Point of Contact:
James Zimmer-Dauphinee (Anthropology)

[email](james.r.zimmer-dauphinee@vanderbilt.edu)  

### Faculty sponsor:
Steven Wernke (Anthropology)

[website](https://stevenwernke.com/)

[email](s.wernke@vanderbilt.edu)
