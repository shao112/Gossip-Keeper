# GossipKeeper
以 Django 網頁框架為主，結合網路爬蟲，製作網路熱門話題論壇。

[HackMD](https://hackmd.io/4LAHtE-QTHSRzIYHc30RBA?both)
```
cd 至專案路徑，執行以下指令
python manage.py runserver
```

## 實作功能

會員制度 (使用者可操作的功能)
  1) 註冊
  2) 登入
  3) 留言
  4) 發布文章
  5) 收藏文章
  6) 更換密碼
  7) 更換頭像
  8) 搜尋關鍵字

關鍵字話題


## 2022.07.20 update
Tokenize -->OK
- Run
```
pip install jieba
pip install nltk
pip install wordcloud

#install package
nltk.download()
```
- WordCloud-Mask Image
  - Background : Black
  - File Type : jpg
