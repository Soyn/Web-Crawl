#!/usr/bin/env python
#-*-coding:utf-8-*-


from modules import spider
from modules import search_engine

from BeautifulSoup import BeautifulSoup, SoupStrainer
import requests

url = "https://github.com/Soyn"
index, graph = spider.CrawlWeb(url, 2)

