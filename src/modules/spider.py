#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
    @Author: Soyn.
    @Brief: A web spider for crawling specified url.
    @CreatedTime: 3/3/16.
    @Soyn: refactor the code, replace the urllib with requests.
           And files structure changed as well.
'''

from search_engine import AddPageToIndex
from BeautifulSoup import BeautifulSoup, SoupStrainer
import requests

def GetPage(url):
    """
    @Brief: Get the web page content.
    :param url: The specified link.
    :return: the page contents
    """
    try:
        import requests
        return requests.get(url).text
    except:
        return ""

def GetAllTheLinks(content):
    """
    @Brief: Extract all the links from the web page.
    :param page: The web page
    :return: The list of url.
    """
    links = []
    for link in BeautifulSoup(content).findAll('a', href=True):
        links.append(link['href'])
    return links

def Union(original_list, added_list):
    """
    @Brief: To union two lists into one.
    :param first_list: Original list.
    :param second_list: The list needs to add.
    :return:
    """
    for element in added_list:
        if element not in original_list:
            original_list.append(element)

def CrawlWeb(seed, max_depth):
    """
    @Brief: The spider to crawl web page from seed.
    :param seed: The seed page.
    :param max_depth: The depth spider will run.
    :return:
    """
    to_crawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    index = {}
    graph = {}  #the graph for ranking

    while to_crawl and depth < max_depth:
        page = to_crawl.pop()
        if page not in crawled:
            content = GetPage(page)
            AddPageToIndex(index, page, content)
            outlinks = GetAllTheLinks(content)
            graph[page] = outlinks
            Union(next_depth, outlinks)
            crawled.append(page)
        if not to_crawl:
            to_crawl, next_depth = next_depth, []
            depth += 1
    return index, graph
