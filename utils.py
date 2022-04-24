from gensim.models import KeyedVectors
import numpy as np
import pandas as pd


def load_embedding(path, binary = True):
    embedding = KeyedVectors.load_word2vec_format(path, binary = binary)
    print('embedding loaded from', path)
    return embedding

def cosine(a, b):
    norm1 = np.linalg.norm(a)
    norm2 = np.linalg.norm(b)
    return np.dot(a, b) / (norm1 * norm2)

def extract_gene_symbol(eid):
    mapping = pd.read_excel("./GeneLists/mapping.xlsx", engine="openpyxl")
    eids = mapping.Entrenz.to_numpy()
    inds = np.where(eids == eid)[0]
    if len(inds) == 0:
        return eid
    else:
        return mapping.iloc[inds[0],0]

def read_genes_from_file(filename):
    genes = []
    with open(filename, "r") as f:
        genes = f.readlines()
    f.close()
    genes = [gene.strip() for gene in genes]
    return genes
