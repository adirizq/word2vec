import sys
import re
import csv
import pickle

from numpy import size

from conllu import parse_incr
from tqdm import tqdm

class Preprocessor():
    def __init__(self) -> None:
        pass


    def clean_sentence(self, sentence):
        sentence = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", sentence)
        sentence = re.sub(r"\'s", "\'s", sentence)
        sentence = re.sub(r"\'ve", "\'ve", sentence)
        sentence = re.sub(r"n\'t", " n\'t", sentence)
        sentence = re.sub(r"\n", "", sentence)
        sentence = re.sub(r",", " , ", sentence)
        sentence = re.sub(r"\!", " ! ", sentence)
        sentence = re.sub(r"\?", " ? ", sentence)
        sentence = re.sub(r"\(", " \( ", sentence)
        sentence = re.sub(r"\)", " \) ", sentence)
        
        sentence = re.sub(r"\'d", " \'d", sentence)
        sentence = re.sub(r"\'re", " \'re", sentence)

        sentence = re.sub(r" \s{2}", " ", sentence)

        return sentence.strip()


    def load_file(self, txt_dataset_dir, csv_dataset_dir, conllu_dataset_dir, tsv_dataset_dir):
        sentences = []

        with open(txt_dataset_dir, "r", encoding="utf-8") as rd:
            for line in tqdm(rd):
                item = line.split("\t")
                sentence = self.clean_sentence(item[1])
                sentences.append(sentence)

        with open(csv_dataset_dir, "r", encoding="utf-8") as f:
            next(f)
            rd = csv.reader(f, delimiter='t')
            for line in tqdm(rd):
                item = ''.join(line).split("\t")
                sentence = self.clean_sentence(item[1])
                sentences.append(sentence)

        with open(conllu_dataset_dir, "r", encoding="utf-8") as f:
            rd = parse_incr(f)
            for line in tqdm(rd):
                item = line.metadata['text']
                sentence = self.clean_sentence(item)
                sentences.append(sentence)
        
        # with open(tsv_dataset_dir) as rd:
        #     for line in tqdm(rd):
        #         if '<' in line:
        #             continue
        #         item = line.split('\t')
        #         sentence = self.clean_sentence(item[0])
        #         if sentence == '':
        #             continue
        #         sentences.append(sentence)

        print(size(sentences))
        print(sentences[:50])