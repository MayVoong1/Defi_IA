# Defi-IA 2021
=====================

<div align="center">
  <img src="images/ia.png" />
</div>

## Table of contents

- [Table of contents](#table-of-contents)
- [Introduction](#introduction)
- [Installation](#installation)
- [Performance](#performance)

## Introduction
The aim of this project is to assign a job to a job description. 

## Installation
    $ git clone https://github.com/MayVoong1/Defi_IA
    $ cd Defi_IA/
    $ sudo pip3 install -r requirements.txt


## Performance

The time required to compute pairwise distance between 100 trajectories (4950 distances), composed from 3 to 20 points (`data/benchmark.csv`) :

| 		         | Euclidan      | Spherical |
| ------------- |:-------------:| -----:|
| discret frechet|0.0659620761871|-1.0|
|dtw | 0.0781569480896 | 0.114996194839|
|edr | 0.0695221424103 | 0.106939792633|
|erp | 0.171737909317 | 0.319380998611|
|frechet | 29.1885719299 | -1.0|
|hausdorff | 0.310199975967 | 0.780081987381|
|lcss | 0.0711951255798 | 0.111418008804|
|sowd grid, precision 5 | 0.164781093597 | 0.159924983978|
|sowd grid, precision 6 | 0.973792076111 | 0.954225063324|
|sowd grid, precision 7 | 7.62574410439 | 7.78553795815|
|sspd | 0.314118862152 | 0.807314872742|





