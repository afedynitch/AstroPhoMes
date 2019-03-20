# AstroPhoMes
A python library implementing astrophysical photomeson models for usage in UHECR sources simulations and related physical scenarios

## Description:
This repository contains tools used for calculating photo-nuclear interactions.
The code provides cross sections for the interaction between photons and nuclei for astrophysical problems.
This is of interest for modelling Ultra-High Energy Cosmic Ray sources and transport.

## Usage
For details see the publication [arXiv](), and for usage refer to the examples folder.

The lib folder contains the main classes which implement the photomeson models.

The model contains methods to obtain the cross sections for a variety of nuclei. 

The particle identification follows the convention below

#### Particle ID convention:
- 2: pi plus
- 3: pi minus
- 4: pi zero
- 100\*A+Z: for nuclei, where Z and A are the proton and total nucleon numbers. For example
	- 100: neutron
	- 101: proton
	- ...
	- 1407: Nitrogen 14 (Z=7, A=14)

## Dependencies:
- os
- sys
- numpy
- utils
- scipy
- pickle
- inspect
- unittest
- itertools
- collections