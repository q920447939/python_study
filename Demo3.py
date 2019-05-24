import requests
from lxml import etree   #xpath
import json


class BTCSpider():

    #成员变量
    base_url = "https://www.chainnode.com"
    forum_url = "/forum/254-"
    user_agent = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
    }

    #构造方法
    def __init__(self, idx):
        self.idx = idx
        pass

    def get_url(self):
        self.response = requests.get(self.base_url + self.forum_url + self.idx, headers=self.user_agent).content.decode(
            "utf-8")
        return

    def purse_data(self):
        # 取出所有的title 和对应的url
        etree_html = etree.HTML(self.response)
         #匹配所有h3 属性class = post-item__title 的子元素a 的文本
        title = etree_html.xpath('//h3[@class="post-item__title"]/a/text()')
          #匹配所有h3 属性class = post-item__title 的子元素a 的href
        href = etree_html.xpath('//h3[@class="post-item__title"]/a/@href')
        #json 数组
        jsonArray = []
        #类似于增强for 循环,有i = 下标，item 等于该下标对应的值
        for i, item in enumerate(title):
            json = {}
            #strip()去掉前后空格    .replace("\n", "") 去掉 \n
            json['title'] = str(item).strip().replace("\n", "")
            json['href'] = self.base_url + href[i]
            jsonArray.append(json)
        return jsonArray

    def save(self, data):
        #字符串转json
        json_dumps = json.dumps(data)
        with open(self.idx + ".json", "w", encoding="utf-8") as f:
            f.write(json_dumps)

    def run(self):
        self.get_url()
        data = self.purse_data()
        self.save(data)


if __name__ == '__main__':
    #int 类型要循环需要加range
    for i in range(6):
        #BTCSpider(str(i+1))  对应的是构造器 ， 将字符串"1"传到对象中
        BTCSpider(str(i+1)).run()