import spacy
import pandas as pd

nlp = spacy.load('en_core_web_lg')

df = pd.read_table('movies.txt')


