#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
    @Author: Soyn
    @Brief: Gets all the links from the web page.
    @CreateTime: 3/3/16.S
"""

def get_page(url):
    """
    @Brief: To get the web page content
    :param url: the link
    :return: the content by string in the url
    """
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

def GetPage(url):
    try:
        if url == 'http://www.xkcd.com/353':
            return """
        <div id="comicLinks">
        Comics I enjoy:<br/>
        <a href="http://threewordphrase.com/">Three Word Phrase</a>,
        <a href="http://www.smbc-comics.com/">SMBC</a>,
        <a href="http://www.qwantz.com">Dinosaur Comics</a>,
        <a href="http://oglaf.com/">Oglaf</a> (nsfw),
        <a href="http://www.asofterworld.com">A Softer World</a>,
        <a href="http://buttersafe.com/">Buttersafe</a>,
        <a href="http://pbfcomics.com/">Perry Bible Fellowship</a>,
        <a href="http://questionablecontent.net/">Questionable Content</a>,
        <a href="http://www.buttercupfestival.com/">Buttercup Festival</a>,
        <a href="http://www.mspaintadventures.com/?s=6&p=001901">Homestuck</a>,
	    <a href="http://www.jspowerhour.com/">Junior Scientist Power Hour</a>
</div>
            """
        else:
            return ""
    except:
        return ""


def GetNextTarget(page):
    """
    @Brief: To extract a link from o page.
    :param page: the web page.
    :return:
    @url: the url we extracts from the page, if not found return None.
    @end_quote: the url's end quote's position in the page, if
    not found return -1.

    """
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0

    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1 : end_quote]
    return url, end_quote


def GetAllTheLinks(page):

    """
    @Brief: Extract all the links from the web page.
    :param page: the web page.
    :return: the the list of url.
    """
    links = []
    while True:
        url, end_position = GetNextTarget(page)
        if url:
            links.append(url)
            page = page[end_position :]
        else:
            break
    return links



def Union(first_list, second_list):
    """
    @Brief: To union two lists into one list.
    :param first_list:
    :param second_list:
    :return: None
    """
    for e in second_list:
        if e not in first_list:
            first_list.append(e)

def CrawlWeb(seed, max_depth):
    """
    @Brief: To crawl the page from the seed.
    @Soyn: Add the code to keep track of the crawl searches depth.(5/3/16).
    :param seed: the seed page.
    :return: the links are crawled.
    """
    to_crawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    index = []
    while to_crawl and depth < max_depth:
        page = to_crawl.pop()
        if page not in crawled:
            content = GetPage(page)
            AddPageToIndex(index, page, content)
            Union(next_depth, GetAllTheLinks(content))
            crawled.append(page)
        if not to_crawl:
            to_crawl, next_depth = next_depth, []
            depth += 1
    return index



index = []
def AddToIndex(index, keyword, url):
    """
    @Brief: Format the index list to store the keyword, urls, and counts.
    Example format data structure: ['good',[["http://www.udacity.com", 0],
    ["http://www.google.com"]]]
    :param index: index list
    :param keyword: the keyword in url
    :param url:
    :return:
    """
    for entry in index:
        if entry[0] == keyword:
            for urls in entry[1]:
                if urls[0] == url:
                    return    # this statement can guarantee
                              # the url only occurs once in the index list
    # not found, add new entry.
    index.append([keyword, [[url, 0]]])

def LookUp(index, keyword):
    """
    @Breif: Look up the urls assiciated with the keyword in index list.
    :param index:
    :param keyword:
    :return:
    """
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None

def AddPageToIndex(index, url, content):
    """
    @Brief: Create the index list which map the keywords
    in content into the url
    :param index: the index list
    :param url: the url
    :param content: web page
    :return:
    """
    words = content.split()
    for word in words:
        AddToIndex(index, word, url)

def RecordUserClick(index, keyword, url):
    """
    @Brief: Record the user clicks counts.
    :param index: the index list
    :param keyword: the keyword user to search
    :param url: the url refers to the keyword
    :return:
    """
    urls = LookUp(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] += 1


