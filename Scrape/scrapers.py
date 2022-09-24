from. import tokenize_eng
from. import language_check
from. import tokenize_cn
from. import today_post_ptt

class PTT:

    def scrape(self):
        # 前六個單詞
        top_six = []

        # 建字詞次數字典
        dict_main = tokenize_eng.dic_create()
        # 抓ptt文章
        list = today_post_ptt.get_ptt()
        sentence = []

        for post in list:
            # 判斷文章語言
            if language_check.check_chinese(post) is False:
                sentence = tokenize_eng.eng_tokenize(post)
            else:
                sentence = tokenize_cn.cn_tokenize(post)

            # 縮排進到迴圈?
            dict_main = tokenize_eng.dic_count(sentence, dict_main)
            count = sorted(dict_main.items(), key=lambda x: x[1], reverse=True)

        for word in range(6):
            top_six.append(count[word][0])

        print(top_six)
        return top_six

class Dcard():
    def scrape(self):
        pass

