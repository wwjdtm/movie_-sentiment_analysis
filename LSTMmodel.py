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


##########
from keras.preprocessing.text import Tokenizer
max_words = 35000
tokenizer = Tokenizer(num_words = max_words)
tokenizer.fit_on_texts(test_pos)
X_train = tokenizer.texts_to_sequences(train_pos)
X_test = tokenizer.texts_to_sequences(test_pos)


##########
import numpy as np
#score_train
#score_test
#2 긍정
#1 보통
#0 부정
y_train = []
y_test = []
for i in range(len(score_train)):
  if score_train[i] == "2":
    y_train.append([0, 0, 1])
  elif score_train[i] == "1":
    y_train.append([0, 1, 0])
  elif score_train[i] == "0":
    y_train.append([1, 0, 0])
for i in range(len(score_test)):
  if score_test[i] == "2":
    y_test.append([0, 0, 1])
  elif score_test[i] == "1":
    y_test.append([0, 1, 0])
  elif score_test[i] == "0":
    y_test.append([1, 0, 0])

y_train = np.array(y_train)
y_test = np.array(y_test)

###################

from keras.layers import Embedding, Dense, LSTM , GRU
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
max_len = 20 # 전체 데이터의 길이를 20로 맞춘다

X_train = pad_sequences(X_train, maxlen=max_len)
X_test = pad_sequences(X_test, maxlen=max_len)


model = Sequential()
model.add(Embedding(max_words, 100))
model.add(LSTM(128)) #or gru
model.add(Dense(3, activation='softmax'))
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy']) #or adam
history = model.fit(X_train, y_train, epochs=10, batch_size=10, validation_split=0.1)
print("\n 테스트 정확도 : {:.2f}%" .format(model.evaluate(X_test, y_test)[1]*100))

