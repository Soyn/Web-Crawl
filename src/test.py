#!/usr/bin/env python
#-*-coding:utf-8-*-


from modules import spider
from modules import search_engine

url = "https://github.com/Soyn"
index, graph = spider.CrawlWeb(url, 2)
