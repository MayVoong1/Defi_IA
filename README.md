# Defi-IA 2021

<div align="center">
  <img src="images/ia.jpg" />
</div>

## Table of contents
- [☀ Introduction](#-introduction)
- [🗃 Dataset](#-dataset)
- [🔧 Installation](#-installation)
- [🏆 Performance](#-performance)

## ☀ Introduction
This project was part of the 5th edition of "Defi IA" organised for students from french-speaking universities. The competition took place between november of 2020 and january of 2021 on the well-known platform Kaggle. The aim was to assign a job to a job description. To resolve this multiclass Machine Learning problem, we had to be aware that the data set is imbalanced and that A REMPLIR

## 🗃 Dataset

We used data from the <a href="https://www.wikiwand.com/en/Common_Crawl">Common Crawl</a>, a non profit organization. We have: 
- a train set of 217197 rows and 3 columns: each row refers to an individual that is identified by his id (first column), a job description (second column) and his sex (third column), 
- a test set of 54300 rows that follows the same structure as the train set, 
- a .csv (train_label.csv) that gathers the correspondence between a job id (0 to 28) and the job.  

## 🔧 Installation 

Note: In the following lines of code, "myenv" refers to the name of the virtual environment. Feel free to change it! 

    $ git clone https://github.com/MayVoong1/Defi_IA
    $ cd Defi_IA/
    
 We use the following commands to create an environment with Python:
 
    $ python -m venv myenv
    $ source myenv/bin/activate
    $ sudo pip3 install -r requirements.txt
    $ pip3 install --user ipykernel
    $ python -m ipykernel install --user --name=myenv
    
#### Another method if you are using Anaconda:
    $ git clone https://github.com/MayVoong1/Defi_IA
    $ cd Defi_IA/
    
 We use the following commands to create an environment:
 
    $ conda create -n myenv python=3.8
    $ conda activate myenv
    $ conda install ipykernel
    $ pip3 install -r requirements.txt
    
## 🏆 Performance

The time required and scores obtained on the test set are gathered in the following table. All the algorithms were runned on a local environment.

| 		         | F1-Score   | Time (in min) |
| ------------- |:-------------:| -----:|
| Logistic regression - Skipgram |0.70520|47|
| MLP - Skipgram | 0.699160 | 210 | 
| Random Forest - Skipgram | 0.58037 | 215 |
| Logistic regression - TF-IDF | 0.72966 | 90 |
| Roberta (Simple Transformer) | 0.79986 |70|

Note: Roberta's F1-Score tends to improve when the batch size is larger. 



