from bs4 import BeautifulSoup
import requests
import time
from urllib import request
from urllib import parse

search_word = "삼성" #검색어 지정
start = 1
end = 300 #마지막 뉴스 지정
title_list = []


class NewsScraper():
    def __init__(self, keyword, end):
        self.title = []
        self.company = []
        self.post_time = []
        self.contents = []
        self.comment = []
        self.keyword = keyword
        self.start = 1
        self.end = end

    def scraping_start(self):
        while True:
            if self.start > self.end:
                break

            url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}&start={}'.format(parse.quote_plus(self.keyword),self.start)
            html = request.urlopen(url)
            soup = BeautifulSoup(html,'html.parser')

            news_list = soup.select("div.news.mynews.section._prs_nws > ul > li")

            for news in news_list:                
                #뉴스제목 뽑아오기
                self.title.append(news.select_one("dl > dt > a")["title"])
                self.company.append(news.select_one("dl > dd > span._sp_each_source").text.split()[0])
                
                try:
                    if news.select_one("dl > dd > a._sp_each_url")["href"] != None:

                        # 기사 세부내용 가져오기
                        url = news.select_one("dl > dd > a._sp_each_url")["href"]
                        html_detail = request.urlopen(url)
                        detail_soup = BeautifulSoup(html_detail, 'html.parser')
                        
                        # 1. 기사 세부내용 - 시간 정보 수집
                        try:
                            self.post_time = detail_soup.select_one("#main_content > div.article_header > div.article_info > div > span.t11").text
                        except AttributeError:
                            continue

                        # 2. 기사 세부내용 - 기사 내용 수집:
                        self.contents = detail_soup.select_one("div#articleBodyContents").text
                                                
                        # 3. 기사 세부내용 - 댓글 수집 :
                        try:
                            comments_list = detail_soup.select_one("div#cbox_module")
                            print(comments_list)
                            for comments in comments_list:
                                self.comment = comments.select_one("")
                                print(self.comment)
                        except TypeError:
                            self.comment.append(None)
                                

                except TypeError:
                    continue

                self.start += 10

        print(self.title)
        print(self.company)


if __name__ == '__main__':
    news_scraping = NewsScraper("인공지능", 20)
    news_scraping.scraping_start()