import pandas as pd
import nltk
dataset = pd.read_table('Indonesian_Manually_Tagged_Corpus2.tsv', header=None, names=['words','tags'])
#dataset.head(10)
#['NN' 'SC' 'VB' 'NNP' 'JJ' 'RB' 'IN' 'Z' 'CD' 'CC' 'PR' 'PRP' 'MD' 'FW'
#'NEG' 'DT' 'NND' 'SYM' 'RP' 'OD' 'X' 'WH' 'UH' 'fw']
#Tulis kode untuk mengoutputkan 10 most frequent words given NN tag
NN_tagged = dataset[dataset['tags']=='fw']
NN_counted = NN_tagged['words'].unique()

cfg = "fw -> "
for token in NN_counted:
    if token == NN_counted[-1]:
        cfg+="'"+token+"'\n"
    else:
        cfg+="'"+token+"' | "

print(cfg)

#with open("mygrammar.cfg", "a") as myfile:
#    myfile.write(cfg)



#grammar1 = nltk.data.load('file:mygrammar.cfg')

