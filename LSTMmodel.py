import csv
from konlpy.tag import Okt
import json
import os
from pprint import pprint
import nltk
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


def read_train_data(filename):
    with open(filename,'r',encoding='utf-8-sig') as f:
      data = [line.split(' ',maxsplit=1) for line in f.read().splitlines()]
    return data

def read_test_data(filename):
    with open(filename,'r',encoding='utf-8-sig') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]
    return data

train_df = read_train_data('data_train.txt')
test_df = read_train_data('data_test.txt')
print(type(train_df))
print(len(train_df))
print(len(test_df))


score_train = []
text_train = []
score_test = []
text_test = []
print(test_df[0])
for i in range(35506):
  score_train+=test_df[i][0]
for i in range(35506):
  text_train+=test_df[i][1:]

for i in range(12000):
  score_test+=train_df[i][0]
for i in range(12000):
  text_test+=train_df[i][1:]

sns.displot(score_train)
sns.displot(score_test)
#########################
okt = Okt()
stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']


def tokenizing(data):
    pos = []
    for sentence in text_train:
        temp_X = []
        temp_X = okt.morphs(sentence, stem=True)  # 토큰화
        temp_X = [word for word in temp_X if not word in stopwords]  # 불용어 제거
        pos.append(temp_X)

    return pos


train_pos = []
test_pos = []

for sentence in text_train:
    temp_X = []
    temp_X = okt.morphs(sentence, stem=True)  # 토큰화
    temp_X = [word for word in temp_X if not word in stopwords]  # 불용어 제거
    train_pos.append(temp_X)

for sentence in text_test:
    temp_X = []
    temp_X = okt.morphs(sentence, stem=True)  # 토큰화
    temp_X = [word for word in temp_X if not word in stopwords]  # 불용어 제거
    test_pos.append(temp_X)


