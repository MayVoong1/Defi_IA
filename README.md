# Defi-IA 2021


<div align="center">
  <img src="images/ia.jpg" />
</div>

## Table of contents

- [Table of contents](#table-of-contents)
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Performance](#performance)

## Introduction
The aim of this project is to assign a job to a job description. A REMPLIR

## Dataset

We used data from the <a href="https://www.wikiwand.com/en/Common_Crawl">Common Crawl</a>, a non profit organization. We have a train set of 217198 rows and 3 columns: each row refer to an individual that is identified by his id (first column), a job description (second column) and his sex (third column). 

## Installation 
    $ git clone https://github.com/MayVoong1/Defi_IA
    $ cd Defi_IA/
    $ sudo pip3 install -r requirements.txt


## Performance

The time required and scores obtained :

| 		         | Score      | Time |
| ------------- |:-------------:| -----:|
| Logistic regression - Skipgram|0.0659620761871|-1.0|
| MLP - Skipgram | 0.0781569480896 | 0.114996194839|
| Random Forest - Skipgram | 0.0695221424103 | 0.106939792633|
| Logistic regression - TF-IDF | 0.171737909317 | 0.319380998611|
| Roberta (Simple Transformer) | 29.1885719299 | -1.0|





