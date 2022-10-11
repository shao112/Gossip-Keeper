import re
import requests
import os
from bs4 import BeautifulSoup
class google_news:

    data = []

    def __init__(self, top_six):
        self.data = top_six
        print("放入完成")
        # print(self.data)

    def google(self):

        # titles = []
        urls = []
        # reg = "[^0-9A-Za-z\u4e00-\u9fa5]"  # 标点符号 #sub(replacement, string[, count=0])
        # data = ['英國','蘋果']  #查詢的字詞
        # data = top_six
        for j in range(0, 6):
            keyword = self.data[j]


            html = "https://news.google.com/search?q=" + keyword + "&hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"
            # ###
            urls.append(html)
            # ###
            # resp = requests.get(html)
            # resp.encoding = 'utf-8'
            # content = resp.text
            # bs = BeautifulSoup(content, 'html.parser')
            # i = 0
            # for news in bs.select('h3'):
            #     if i >= 10:
            #         break 
            #     url = news.select('a')[0]['href']
            #     urls.append(url)
            #     title = news.select('a')[0].text
            #     titles.append(title)
            #     i+=1
        return urls

# <a href="url">title</a>


