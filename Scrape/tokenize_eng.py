import string
import nltk
from nltk.corpus import wordnet as wordnet
# from nltk.stem import WordNetLemmatizer
# ----------------------------------------------------------------
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
# ----------------------------------------------------------------
# motorcar = wordnet.synset('car.n.01')
# motorcar.hypernyms_paths()
# print(motorcar.hypernym_paths())

# text = """Western France is facing a "heat apocalypse", experts have warned, as extreme temperatures continue to hit much of Europe.

# Temperatures could reach record levels in 15 regions of the southwest, with firefighters battling wildfires and thousands forced to evacuate.

# Blazes in Spain, Portugal and Greece have forced thousands more to flee.

# Record temperatures are also expected in parts of the UK, which has its first ever red extreme heat warning in place.

# Wildfires in France in recent days have forced over 24,000 people to flee, with emergency shelters set up for evacuees.

# Gironde, a popular tourist region in the southwest, has been hit particularly badly, with firefighters battling to control fires which have destroyed over 14,000 hectares (34,000 acres) of land since last Tuesday."""

# 要下載的東西，請勿亂拿掉註解，不然每次開啟網頁都會跑這個
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('stopwords')

def add(x, y):
    z = x+y
    return z

#路徑要改
def stopwords_eng_create():
    stopwords = []
    with open('C:\\Users\\rauou\\django\\GossipKeeper\\Scrape\\stopword\\stopwords_eng.txt', 'r', encoding="utf-8") as f:
        stopwords = [word.strip('\n') for word in f]
        return stopwords

def eng_tokenize(text):
    text = text.replace('"', '')
    sentences = nltk.sent_tokenize(text.lower())
    # 基本斷詞 -->OK
    tokens = [nltk.tokenize.word_tokenize(sent) for sent in sentences]

    # POS (詞性標記) -->OK
    pos = [nltk.pos_tag(token) for token in tokens]
    for item in pos:
        print(item)

    # word_lemm 各單詞詞性清單(只有詞性)
    # p 各行內容
    # word = p[0,0]
    # tag = p[0,1]

    word_lemm = []

    for p in pos:
        tag_lemm = []
        for word, tag in p:
            if tag.startswith('N'):
                tag_lemm.append(nltk.corpus.wordnet.NOUN)
            elif tag.startswith('J'):
                tag_lemm.append(nltk.corpus.wordnet.ADJ)
            elif tag.startswith('V'):
                tag_lemm.append(nltk.corpus.wordnet.VERB)
            elif tag.startswith('R'):
                tag_lemm.append(nltk.corpus.wordnet.ADV)
            else:
                tag_lemm.append(nltk.corpus.wordnet.NOUN)
        word_lemm.append(tag_lemm)

    print("\n\n")
    print(word_lemm)

    # 字形還原 -->OK
    lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()

    tokens = []
    x = -1
    for p in pos:
        x += 1
        for n in range(len(p)):
            tokens.append(lemmatizer.lemmatize(p[n][0], pos=word_lemm[x][n]))

    # 扁平化解析式 --> Wrong Code
    # tokens = [lemmatizer.lemmatize(p[n][0], pos=word_lemm[n])
    #            for p in pos for n in range(len(p))]

    # 停用詞 -->OK
    nltk_stopwords = nltk.corpus.stopwords.words('english')

    tokens = [token for token in tokens if token not in nltk_stopwords]

    # punctuation remove setting -->OK
    tokens = [token for token in tokens if token not in string.punctuation]
    for token in tokens:
        print(token)

    return tokens
# ----------------------------------------------------------------


# 字詞出現次數統計 -->OK

def dic_create():

    dict_create = dict()
    return dict_create


def dic_count(tokens, dict):

    dict_count = dict

    for word in tokens:
        if word not in dict_count:
            dict_count[word] = 1
        else:
            dict_count[word] += 1

    # sort
    # dict_count = sorted(dict_count.items(), key=lambda x: x[1])
    # print(dict_count)

    return dict_count
# ----------------------------------------------------------------

# 轉字串


def dict_to_string(dict_count):
    dict_string = ''
    for word, count in dict_count:
        dict_string += (word + ' ')
    print(dict_string)

    return dict_string

