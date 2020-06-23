# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DaumNewsItem


class DaumNewsSpider(CrawlSpider):
    name = 'news'

    start_urls = ['https://news.daum.net/breakingnews/digital/internet', 'https://news.daum.net/breakingnews/digital/science',
     'https://news.daum.net/breakingnews/digital/game', 'https://news.daum.net/breakingnews/digital/it', 'https://news.daum.net/breakingnews/digital/device',
     'https://news.daum.net/breakingnews/digital/mobile', 'https://news.daum.net/breakingnews/digital/software', 'https://news.daum.net/breakingnews/digital/others',
     'https://news.daum.net/breakingnews/sports/worldbaseball', 'https://news.daum.net/breakingnews/sports/soccer', 'https://news.daum.net/breakingnews/sports/baseball',
     'https://news.daum.net/breakingnews/sports/others', 'https://news.daum.net/breakingnews/sports/esports', 'https://news.daum.net/breakingnews/sports/worldsoccer',
     'https://news.daum.net/breakingnews/editorial',
     'https://news.daum.net/breakingnews/society/affair','https://news.daum.net/breakingnews/society/people', 'https://news.daum.net/breakingnews/society/labor',
     'https://news.daum.net/breakingnews/society/environment', 'https://news.daum.net/breakingnews/society/education',
     'https://news.daum.net/breakingnews/economic/finance', 'https://news.daum.net/breakingnews/economic/employ', 'https://news.daum.net/breakingnews/economic/stock',
     'https://news.daum.net/breakingnews/economic/consumer',
     'https://news.daum.net/breakingnews/entertain/drama', 'https://news.daum.net/breakingnews/entertain/variety',
     ]

    # 링크 크롤링 규칙(정규표현식)
    rules = [
        # IT 분야 - 인터넷, 과학, 게임, 휴대폰통신, IT기기, 통신_모바일, 소프트웨어, Tech일반
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/digital/internet\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/digital/science\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/digital/game\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/digital/it\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/digital/device\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/digital/mobile\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/digital/software\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/digital/others\?page=\d$'), callback='parse_headline'),
        # 스포츠 분야 - 해외야구, 축구, 야구, 스포츠일반, 해외축구
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/sports/worldbaseball\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/sports/soccer\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/sports/baseball\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/sports/others\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/sports/worldsoccer\?page=\d$'), callback='parse_headline'),
        # 칼럼
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/editorial\?page=\d$'), callback='parse_headline'),
        # 사회 - 사건/사고, 인물, 노동, 환경, 교육, 
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/society/affair\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/society/people\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/society/labor\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/society/environment\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/society/education\?page=\d$'), callback='parse_headline'),
        # 금융 - 금융, 취업직장인, 주식, 부동산, 생활경제
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/economic/finance\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/economic/employ\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/economic/stock\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/economic/estate\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/economic/consumer\?page=\d$'), callback='parse_headline'),
        # 연예 - 가요음악, 드라마, 예능
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/entertain/drama\?page=\d$'), callback='parse_headline'),
        Rule(LinkExtractor(allow=r'https://news.daum.net/breakingnews/entertain/variety\?page=\d$'), callback='parse_headline'),
    ]

    def parse_headline(self, response):
        # URL 로깅
        self.logger.info('Response: %s' % response.url)
        item = DaumNewsItem()

        news_topic = response.url.split('/')[4]
        news_topic_detail = response.url.split('/')[5].split('?')[0]

        # 기사 찾기
        article_list = response.css('ul.list_news2.list_allnews > li > div')
        for article in article_list:
            news_headline = article.css('strong > a::text').extract_first().strip()
            news_url = article.css('strong > a::attr(href)').extract_first().strip()
            news_company = article.css('span.info_news::text').extract_first().strip()

            # meta를 통해 item 객체를 parse_article에 전달
            yield scrapy.Request(response.urljoin(news_url), self.parse_article, 
            meta={'news_topic': news_topic, 'news_topic_detail': news_topic_detail,
            'news_headline': news_headline, 'news_url': news_url, 'news_company': news_company})

    def parse_article(self, response):
        # ('span.info_view > span:nth-child(2)::text') 는 기사 시간을 추출 하기 위함
        news_time = ' '.join(response.css('span.info_view > span:nth-child(2)::text').extract_first().split(' ')[1:])
        # ('#harmonyContainer > section > p::text')는 contents 본문 p태그들을 의미
        news_contents = ' '.join(response.css('#harmonyContainer > section > p::text').extract())
        news_comments = response.css('span.alex-count-area::text').extract_first().strip()
        item = DaumNewsItem()
        # yield DaumNewsItem(news_item=news_item, news_url=news_url, news_company=news_company)
        item['news_topic'] = response.meta['news_topic']
        item['news_topic_detail'] = response.meta['news_topic_detail']
        item['news_headline'] = response.meta['news_headline']
        item['news_url'] = response.meta['news_url']
        item['news_company'] = response.meta['news_company']
        item['news_time'] = news_time
        item['news_contents'] = news_contents
        item['news_comments'] = news_comments

        yield item


