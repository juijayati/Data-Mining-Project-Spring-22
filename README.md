# Data-Mining-Project-Spring-22

* [Installation](#pip)
* [Text Corpora and Named Entity Recognition (NER)](#ner)
* [Data Overview](#overview)
* [Training Word2Vec Embeddings](#w2v)
* [Exploratory Analysis](#vis)
* [Evaluation Datasets](#dataset)
* [Intrinsic Evaluation](#intrinsic)
* [Extrinsic Evaluation](#extrinsic)

## Installation
<a name="pip"></a>
git clone https://github.com/juijayati/Data-Mining-Project-Spring-22.git

pip install -r requirements.txt

## Text Corpora and Named Entity Recognition (NER)
<a name="ner"></a>
We used PubMed articles related to wound healing for training the word vectors and used PubTator to annotate the gene and protein mentions in the abstracts. 

File: data_download_and_preprocessing.ipynb

## Data Overview
<a name="overview"></a>
We plotted the distributions of the annotated corpora

File: data_overview.ipynb

## Training Word2Vec Embeddings
<a name="w2v"></a>
We used Gensim Word2Vec for training the word vectors.

File: train_w2v.ipynb

## Exploratory Analysis
<a name="vis"></a>
File: visualize.ipynb

## Evaluation Dataset
<a name="dataset"></a>
The evaluation datasets are stored in the Datasets folder.

## Intrinsic Evaluation
<a name="intrinsic"></a>
File: intrinsic_evaluation.ipynb

## Extrinsic Evaluation
<a name="extrinsic"></a>
File: extrinsic_evaluation.ipynb




