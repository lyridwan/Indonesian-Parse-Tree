import pandas as pd
dataset = pd.read_table('Indonesian_Manually_Tagged_Corpus2.tsv', header=None, names=['words','tags'])
#dataset.head(10)

#Tulis kode untuk hitung frequency tiap jenis tag
counted = dataset['tags'].value_counts()

#Tulis kode untuk mengoutputkan 10 most frequent tags
#print('10 most frequent tags:', counted.head(10), sep='\n')

#Tulis kode untuk mengoutputkan 10 most frequent words given NN tag
#NN_tagged = dataset[dataset['tags']=='NN']
#NN_counted = NN_tagged['words'].value_counts()
#print('\n10 most frequent words given NN tag:', NN_counted.head(10), sep='\n')

#Tulis kode untuk mengoutputkan 5 kata yang memiliki tag lebih dari 1, beserta tag2nya.
grouped_by_word = dataset.groupby('words')['tags'].unique()
word_and_mt1_tags = grouped_by_word[grouped_by_word.apply(lambda x: len(x)>1)]
print('\nWords and more than 1 tags with all tags:', word_and_mt1_tags.sample(5), sep='\n')

import nltk
from nltk import hmm

# Fungsi membuat list of list of tuple
# low: List of Words
# sep: separator (pemisah dalam kalimat, titik)
def c_list_of_sentences(low, sep):
    sentence = []
    sentences = []
    for word in low:
        sentence.append(word)
        if word == sep:
            sentences.append(sentence)
            sentence = []
    return sentences

#train_data adalah list yang menampung semua kalimat dengan format di atas
#Tulis kode untuk transform kalimat ke format [('kata1','tag1'),('kata2','tag2'),('kata3','tag3')]
#lalu simpan semua kalimat dalam list train_data

list_of_words = dataset.to_records(index=False).tolist()
sep = ('.', 'Z')
    
train_data = c_list_of_sentences(list_of_words, sep)

trainer=hmm.HiddenMarkovModelTrainer()
tagger=trainer.train_supervised(train_data)

grammar1 = nltk.data.load('file:mygrammarbackup.cfg')
parser = nltk.ChartParser(grammar1)

def parsetree (args):
    sent = args.split()

    tagged_text = tagger.tag(sent)
    pos_tags = [pos for (token,pos) in tagged_text]
    print (tagged_text)

    print("training...")
    temp = ""
    for tree in parser.parse(sent):
        if tree != temp:
            print("parsing grammar...")
            print(tree)
            tree.draw()
        temp = tree

#parsetree("saya membaca buku tiga halaman di halaman sekolah")
#parsetree("kami bangkit bersama dengan keterpurukan")
parsetree("ibu dan ayah pergi ke pasar di Jakarta")
parsetree("banjir sudah melanda kota Jakarta tiga tahun silam")

