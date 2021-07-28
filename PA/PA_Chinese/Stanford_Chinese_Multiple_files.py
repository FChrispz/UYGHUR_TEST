# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 19:53:30 2021

@author: Chris
"""
import sys
import stanza
import os.path
import os
import glob
from pathlib import Path

Path('/root/dir/sub/file.ext').stem

stanza.download('zh', processors='tokenize,lemma,pos,ner')
stanza.download(lang="zh-hans",package=None,processors={"sentiment":"ren"})
nlp = stanza.Pipeline('zh', processors='tokenize,lemma,pos,ner,sentiment')

Stanford_PC_Chinese = glob.glob('D:/Users/Chris/Desktop/PA/PA_Chinese_raw_files/*.txt')

outfile = open('Stanford_PA_Chinese_all.utf8', 'w+', encoding="utf-8")
sys.stdout = outfile

for file in Stanford_PC_Chinese:

    with open(file, 'r', encoding="utf-16") as file_input:  
        print(Path(file).stem)      
        for line in file_input:
            doc = nlp(line)
            print(line)
            
            #i=1
            #for i,sentence in enumerate(doc.sentences):
                #print(f'\n====== Sentence '+str(i)+' tokens =======')
                #print(*[f'id: {token.id}\ttext: {token.text}' for token in sentence.tokens], sep='\n')
            for sent in doc.sentences:
                    for word in sent.words:
                        print(f'word: {word.text}\tlemma: {word.lemma}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}')   
                    print('\n')
            print(*[f'entity: {ent.text}\ttype: {ent.type}' for ent in doc.ents], sep='\n')
            #for sentence in enumerate(doc.sentences):
            print(f'\nSentence sentiment= '+str(sent.sentiment))
            print('\n')
             #i=i+1