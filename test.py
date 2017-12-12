import pandas as pd
import nltk
dataset = pd.read_table('Indonesian_Manually_Tagged_Corpus2.tsv', header=None, names=['words','tags'])
#dataset.head(10)

#Tulis kode untuk mengoutputkan 10 most frequent words given NN tag
#NN_tagged = dataset[dataset['tags']=='NN']
#NN_counted = NN_tagged['words'].unique()


grammar1 = nltk.data.load('file:mygrammar.cfg')
for p in grammar1.productions():
    print(p)
