# -*- coding: utf-8 -*-
import scrapy
import re


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()
        utf8 = response.xpath('//input[@name="utf8"]/@value').extract_first()
        post_data = {
                "commit": "Sign in",
                "utf8": utf8,
                "authenticity_token": authenticity_token,
                "login": "q920447939",
                "password": "Liming19940820",
                "webauthn-support": "supported"
            }
        yield scrapy.FormRequest(
            url="https://github.com/session",
            callback=self.parseItem,
            formdata=post_data
        )

    def parseItem(self, response):
        with open("1.html", "w", encoding="utf-8") as f:
            f.write(response.body.decode("utf-8"))
        return
