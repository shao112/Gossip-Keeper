from pyexpat import model
import hanlperceptron
import sys
# import time
import re

#路徑要改
def stopwords_create():
    stopwords = []
    with open('C:\\Users\\rauou\\django\\GossipKeeper\\Scrape\\stopword\\stopwords.txt', 'r', encoding="utf-8") as f:
        stopwords = [word.strip('\n') for word in f]

    return stopwords

reg = "[^0-9A-Za-z\u4e00-\u9fa5]"

segmenter2 = hanlperceptron.Segmenter()


#路徑要改
segmenter2.load('C:///Users/rauou/django/GossipKeeper/Scrape/stopword/cws.pkl')
segmenter2.load_custom_dict('C:///Users/rauou/django/GossipKeeper/Scrape/stopword/dict.txt')

def cn_tokenize(text):
    input_str = text
    clear_str = re.sub(reg, '',input_str)
    list = segmenter2.segment(clear_str)

    list = [token for token in list if token not in stopwords_create() and len(token)!=1 and  not token.isdigit()]
    
    return list

