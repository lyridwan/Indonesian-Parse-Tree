import pandas as pd
import nltk

grammar1 = nltk.data.load('file:mygrammarbackup.cfg')

sent = "saya berangkat sekolah".split()
parser = nltk.ChartParser(grammar1)

for tree in parser.parse(sent):
    print("parsing grammar...")
    print(tree)
    tree.draw()
