# -*- coding: utf-8 -*-
import requests

print(requests.get("http://ip.zdaye.com/dayProxy/ip/312007.html", headers={
    "Referer": "http://ip.zdaye.com/dayProxy/2019/4/1.html",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}).content.decode('gb2312'))
