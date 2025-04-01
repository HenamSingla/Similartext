import numpy as np, pandas as pd
from nltk import RegexpTokenizer
from gensim.models import Word2Vec
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity


def create_tokens(frame):
    tokens = []
    for i in range(len(frame)):
        j=tknzr.tokenize(str(frame[i]))
        tokens.append(j)
    return tokens


def remove_stop_words(tokkens):
    newtokens = []
    for i in range(len(tokkens)):
        ts = [w for w in tokkens[i] if not w in stp_wrds]
        newtokens.append(ts)
    return newtokens


def create_word_vectors(x):
    return Word2Vec(x, min_count=1)


def create_sen_vectors(t,v):
    s = []
    for i in range(len(t)):
        j = 0
        sv = [0]*100
        for j in range(len(t[i])):
            w = t[i][j]
            sv = sv+v[w]
        s.append(sv)
    return s


def cosine_score(t,s):
    l = len(t)
    z = np.asarray([-1]*l*l)
    z = z.reshape(l,l)
    s = np.asarray(s)
    score = (cosine_similarity(s)-z)/2
    return pd.DataFrame(score)


def check(i):
    if(i==0):
        l[i].append(titles[i])
    elif(i>=1):
        j=0
        k=0
        for j in range(i):
            if(scores[i][j]>=0.9):
                l[j].append(titles[i])
                k=1
                break
        if(k==0):
            l[i].append(titles[i])


data = pd.read_csv("headlines.csv", sep="|")
titles = data['Title']
tknzr = RegexpTokenizer(r'\w+')
l = [[] for title in range(len(titles))]

stp_wrds=set(stopwords.words('english'))

tkns = create_tokens(titles)
tkns_wo_stp = remove_stop_words(tkns)
wrdvec = create_word_vectors(tkns_wo_stp)
senvec = create_sen_vectors(tkns_wo_stp,wrdvec)
scores = cosine_score(tkns,senvec)

m=0
print('Clustering similar meaning sentences, please wait...')
for m in range(len(titles)):
    check(m)

x = [y for y in l if y != []]

df = pd.DataFrame(x)
df.to_csv("result_similar headlines stacked together.csv", index=False, header=False)
print('Task complete, results saved in file: result_similar headlines stacked together.csv')
