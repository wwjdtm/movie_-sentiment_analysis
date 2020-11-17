from konlpy.tag import Okt
import json
import os
from pprint import pprint

def read_train_data(filename):
    with open(filename,'r') as f:
        data = [line.split(' ',maxsplit=1) for line in f.read().splitlines()]

    return data

def read_test_data(filename):
    with open(filename,'r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]
    return data

train_df = read_train_data('naver_movie.txt')
test_df = read_test_data('ratings_test.txt')
print(type(train_df))
print(train_df[0])
okt = Okt()

def tokenizing(docs):
    return ['/'.join(t) for t in okt.pos(docs,norm=True, stem=True)]

train_pos = []
test_pos = []
for row in train_df:
    try:
        train_pos0 = [tokenizing(row[1]),row[0]]
        train_pos.append(train_pos0)
    except:
        pass

# for row in test_df:
#     try:
#         test_pos0 = [tokenizing(row[1]), row[2]]
#         test_pos.append(test_pos0)
#     except:
#         pass

pprint(train_pos[0])
