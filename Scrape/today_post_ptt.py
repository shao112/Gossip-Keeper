from bs4 import BeautifulSoup
import requests
import re


def get_ptt():

    # 掛上headers模擬使用者讀取網頁的行為
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    # 目標網站
    url = "https://www.pttweb.cc/hot/all/today"
    # 發出 get請求
    resp = requests.get(url, headers=headers)
    # 網頁編碼
    resp.encoding = 'utf-8'
    # 透過 BeautifulSoup 進行網頁解析
    soup = BeautifulSoup(resp.text, 'html.parser')
    # 找出所有 div區塊中 帶有目標class名的元素
    divs = soup.find_all(
        'div', 'e7-right-top-container e7-no-outline-all-descendants')

    # 新增個list存取爬下來的內容
    articles = []
    # 換個網頁爬文章內容
    root = 'https://www.ptt.cc'
    # 在BeautifulSoup整理好的 divs中的各個區塊把需要的元素取出
    for div in divs:
        # 文章標題
        title = div.find('span', 'e7-show-if-device-is-not-xs').text

        # 拿掉前面分類
        if title[0:4] == "Re: ":
            title = re.sub(r'.', '', title, count=9)
        else:
            title = re.sub(r'.', '', title, count=5)

        # 拿掉特殊符號
        specialChars = "-】~!#$%^&*()/／?？!！「」.：:（）…，、。\"\''\u3000'"
        for specialChar in specialChars:
            title = title.replace(specialChar, '')
        # print(title)

        # 變串列 刪空白
        articles.append(title.replace(' ', ''))

    return articles
