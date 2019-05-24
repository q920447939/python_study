# -*- coding: utf-8 -*-
from copy import deepcopy

import scrapy
from urllib import parse
import json
import re


class JdbookSpider(scrapy.Spider):
    name = 'jdbook'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath('//div[@class="mc"]/dl/dt')  # 大分类
        flg = True
        for dt in dt_list:
            if flg:
                """
                    解析小分类
                """
                next_dd = dt.xpath('./following-sibling::dd[1]')
                for a in next_dd[0].xpath('.//a'):
                    json_small_cat = {}
                    json_small_cat["d_name"] = dt.xpath('./a/text()').extract_first()  # 大分类名称
                    d_source_url = parse.urljoin(response.url, dt.xpath('./a/@href').extract_first())  # 大分类地址
                    json_small_cat["d_source_url"] = d_source_url

                    json_small_cat["s_name"] = a.xpath('./text()').extract_first()
                    detail_url = parse.urljoin(response.url, a.xpath('./@href').extract_first())
                    json_small_cat["s_source_url"] = detail_url  # 小分类地址

                    yield scrapy.Request(
                        detail_url,
                        callback=self.parse_small_cat,
                        meta={
                            "d": deepcopy(json_small_cat)
                        }
                    )
                flg = False

        pass

    def parse_small_cat(self, response):
        li_list = response.xpath('//div[@id="plist"]//li[@class="gl-item"]')
        temp_json = response.meta['d']
        for li in li_list:
            #temp_json['book_img'] = "https:" + li.xpath('.//div[@class="p-img"]//img/@src').extract_first()
            temp_json["book_name"] = li.xpath('//div[@class="p-name"]//em/text()').extract_first().replace("\n","").strip()
            #temp_json['book_introduce'] = li.xpath('//div[@class="p-name"]//i/text()').extract_first()  # 介绍
            #temp_json['book_author'] = li.xpath('//div[@class="p-bookdetails"]/span[@class="p-bi-name"]//a/text()').extract()  # 作者
            prees_list = li.xpath('//div[@class="p-bookdetails"]/span[@class="p-bi-store"]/a/@title').extract()

            #temp_json["book_press"] = [item.replace("\n","").strip() for item in prees_list ]  # 出版社
            temp_json["book_publish_date"] = li.xpath(
                '//div[@class="p-bookdetails"]/span[@class="p-bi-date"]/text()').extract_first().replace("\n","").strip()  # 发布日期
            # comment = li.xpath('//div[@class="p-commit"]//a/text()').extract_first()
            # print("comment:",comment)
            # if comment is not None:
            #     number = re.findall(r'[0-9]+', comment)
            #     if str(comment).find("万"):
            #         comment = number + "0000"
            # temp_json['book_comment'] = comment  # 评论

            # 价格
            try:
                scrapy.Request(
                    url='https://p.3.cn/prices/mgets?skuIds=J_{}'.format(
                        li.xpath('./div[@class="gl-i-wrap j-sku-item"]/@data-sku')),
                    callback=self.parse_price,
                    meta={
                        "d", temp_json
                    }
                )
            except Exception as e:
                print(temp_json)
                print("exception:", e)
                pass
        pass

    def parse_price(self, response):
        temp_json = response.meta['d']
        temp_json['price'] = json.loads(response.body)[0]['p']
        print("temp_json:", temp_json)
        pass
