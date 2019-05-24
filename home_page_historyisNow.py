#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
# 抓取历史上的今天
import requests
import json
from fake_useragent import UserAgent
from lxml import etree  # xpath
import json
import pymysql
import time

db = pymysql.connect("localhost", "root", "123456", "world")
cursor = db.cursor()


class SpiderHistory():
    url = "http://www.lssdjt.com"
    request = requests.Session()
    ua = UserAgent()

    def __init__(self):
        return

    def run(self):

        try:
            # 先查询mysql 有没有抓取今天的记录
            mres = cursor.execute(
                "select 1 from `history_now` "
                "where DATE_FORMAT(create_time,'%Y-%m-%d') ='" + time.strftime('%Y-%m-%d', time.localtime(time.time()))
                + "'  limit 1")
            if mres == 1:
                print("已保存当日记录")
                return

            resp = self.request.get(self.url, headers={'User-Agent': self.ua.random})
            if resp.status_code != 200:
                print("返回值错误")
                return
            etree_html = etree.HTML(resp.content.decode("utf-8"))
            detail_href = etree_html.xpath('//div[@id="slideshow"]/div/p/a/@href')
            image_url = etree_html.xpath('//div[@id="slideshow"]/div//img/@src')
            image_title = etree_html.xpath('//div[@id="slideshow"]/div//a/text()')
            for i, item in enumerate(detail_href):
                insert_ = "INSERT INTO `history_now` ( `href`, `image_url`, `image_title`) " \
                          "VALUES ('" + (self.url + item) + "', '" + image_url[i] + "','" + image_title[i] + "')"
                cursor.execute(insert_)
                db.commit()
        finally:
            db.close()


if __name__ == '__main__':
    SpiderHistory().run()
