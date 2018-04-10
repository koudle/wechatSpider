import os
import time
import wechatsogou
from wechatsogou import WechatSogouConst
from pprint import pprint
import pdfkit
import savepdf

ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)

categorys = [WechatSogouConst.hot_index.hot,WechatSogouConst.hot_index.recommendation,
             WechatSogouConst.hot_index.duanzi,WechatSogouConst.hot_index.health,
             WechatSogouConst.hot_index.sifanghua,WechatSogouConst.hot_index.gossip,
             WechatSogouConst.hot_index.life,WechatSogouConst.hot_index.finance,
             WechatSogouConst.hot_index.car,WechatSogouConst.hot_index.technology,
             WechatSogouConst.hot_index.fashion,WechatSogouConst.hot_index.mummy,
             WechatSogouConst.hot_index.dianzan,WechatSogouConst.hot_index.travel,
             WechatSogouConst.hot_index.job,WechatSogouConst.hot_index.food,
             WechatSogouConst.hot_index.history,WechatSogouConst.hot_index.study,
             WechatSogouConst.hot_index.constellation,WechatSogouConst.hot_index.sport]

dir = os.path.dirname(__file__)  + "/" + time.strftime("%Y-%m-%d", time.localtime())

if os.path.exists(dir):
    os.rmdir(dir)
else:
    os.mkdir(dir)

count = 0

for category in categorys:
    for page in range(1,5):
        articles = ws_api.get_gzh_article_by_hot(category,page)
        for article in articles:
            start = time.time();
            savepath = dir + "/" + str(count) + "_" + article.get("gzh").get("wechat_name") + "_" +\
                       time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(article.get('article').get('time'))) + "_" +\
                       article.get('article').get('title')+".pdf"
            url = article.get('article').get('url')
            count += 1
            pprint(savepath)
            pprint(url)
            #pdfkit.from_url(url,savepath)
            savepdf.savetopdf(savepath,url)
            pprint(time.time() - start)

# pprint(len(articles))
# for i in articles:
#     pprint(i)
#     pprint("\n")