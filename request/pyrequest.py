# -*- coding: utf-8 -*-
# @author: Mingchun Wu
"""pyrequest."""
import requests

# 申请访问网址，获取数据
# response = requests.get("http://www.shuquge.com/txt/8659/2324752.html")
response = requests.get("http://zs.ccnu.edu.cn/info/1026/4947.htm")
# 万能解码，避免乱码
response.encoding = response.apparent_encoding
print(response.text)
