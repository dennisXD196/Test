# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:52:45 2019

@author: Dennis
"""
import sys
import pickle
import requests
from datetime import datetime
from bs4 import BeautifulSoup


def get_date(news_block_node):
    date_string = news_block_node.find(class_="news_date").string.split('|')[0][2:-1]
    return(datetime.strptime(date_string, '%Y.%m.%d').strftime('%Y-%m-%d'))
    
def get_title(news_block_node):
    return news_block_node.find(class_="news_title").a.string

def get_link(news_block_node):
    return news_block_node.find(class_="news_title").a.get('href')
"""
以上三個皆是找到標籤並印出內容

"""
def get_content(link):    #####
    r = requests.get(link)
    r.encoding = "UTF-8"
    soup = BeautifulSoup(r.text, 'html.parser')
    article_node = soup.find(itemprop='articleBody')
    article = article_node.get_text()
    
    """    new part    """
    txt_temp=article.replace("\n", "")
    
    return txt_temp[0:txt_temp.find("\r")]
"""
找到標籤並印出內容，但是現在會有個擾人的廣告 - Dable
我以我加了一行去除廣告
"""

def get_news_info(each_news):
    date  = get_date(each_news)
    title = get_title(each_news)
    link  = get_link(each_news)
    content = get_content(link)
    
    info = {'date' : date,
            'title': title,
            'link' : link,
            'content': content}
    return(info)
"""
使用函數印出
date  title  link  content

"""

def get_page_news(page_url):
    r = requests.get(page_url)
    r.encoding = "UTF-8"

    soup = BeautifulSoup(r.text, 'html.parser')
    news_blocks = soup.find_all(class_="news-list-item clearfix ")
    
    news = []
    for each_news in news_blocks:
        try:
            news_info = get_news_info(each_news)
#             print(get_title(each_news))
        except:
#             print('-------{}-------'.format())
            pass

        news.append(news_info)
    return(news)
"""
針對個別 URL 用 BeautifulSoup 展開，找到所有 <div class="news-list-item clearfix ">
並對個別新聞區塊使用 get_news_info()

"""

def get_new_talk_news(from_page=1, end_page=270, url="https://newtalk.tw/news/subcategory/2/政治/"):
    print("page_number from {} to {}".format(from_page, end_page -1))
    data = []
    for page_number in range(from_page, end_page):
        print("page_number: {}".format(page_number))
        data = data + get_page_news( url+str(page_number) )
    
    print('done')
    return(data)
"""
從 url (1-270 頁) 使用 get_page_news 並把所有的資料都存在 data 裡面

"""


data = get_new_talk_news(from_page=1, end_page=270)#主程式

##############################################################################









get_content("https://newtalk.tw/news/view/2019-02-26/212664")































































