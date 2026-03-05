# PHB production optimization in Rhodopseudomonas palustris

## Overview

Plastic pollution from fossil-fuels ia a major global environmental challenge. Microbial bioplastics such as polyhydroxybutyrate (PHB) is a promising biodegradable alternative. However, the high substrate and operational costs associated with PHB production remain a major barrier to large-scale development and comercialization. 
This project develops an hybrid computational framework to identify cost-efficient and biologically feasible PHB production strategies using the phototrophic bacterium Rhodopseudomonas palustris. 
This framework combines:
- Genome-scale metabolic modeling (GEM)
- Machine learning surrogate modeling
- Pareto multi-objective optimization
- Thermodynamics-based flux analysis (TFA)

Together, these approaches aenable exploration of large metabolic and environmental design spaces that otherwise would be impractical to evaluate to propose cost-effective production strategies that can be validated experimentally. 

## Data

Experimental data from Buitron et al. 2025 was used. 
Additionally, literature data was collected and used for definining the substrates and calculating their uptake flux ranges used in GEM. 

## Repository Structure

phb-optimization-rpalustris/
│
├── notebooks/ # Jupyter notebooks for analyses
├── src/ # Python utility modules
├── data/ # Input datasets
└── README.md

## Clone the repository

To download this repository to your local machine:

```bash
git clone https://github.com/hector-ahg/phb-optimization-rpalustris.git
cd phb-optimization-rpalustris

## Author
Hector Hernandez Gonzalez, PhD in Computational Biology
