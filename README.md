# Image and News Scraping with Django and Scrapy

> 멀티캠퍼스 이미지 분석 AI 과정 1차 미니 프로젝트(2020년 3월 30일 ~ 4월 24일)

이미지 기반 실무 최종 프로젝트 수행 전 수행한 미니 프로젝트입니다. 
프로젝트명은 **'Django와 Scrapy 프레임워크를 이용한 Image 및 Daum News 스크래이핑 웹 서비스'**로 최종 프로젝트 수행 시, **수 십만 장의 이미지 데이터 수집에 도움이 되는 도구로 활용**하고 싶었기 때문이며, 또한 텍스트 문자에 대한 자연어 처리로 주제 및 핵심 내용 요약 등의 작업을 개인적인 목적으로 수행해 보고 싶었기 때문입니다. 

<img src="https://user-images.githubusercontent.com/60699771/85430431-11c73080-b5bb-11ea-9914-0cc7401bcdb0.gif" width=60% >

* 기능

  ![image-20200623233829360](https://user-images.githubusercontent.com/60699771/85418079-52b74900-b5ab-11ea-86c9-3978439d3e85.png)



## 활용 프레임워크

* Django : 3.0.3
* Scrapy: 2.1.0
* MySQL: 8.0.19
* ElasticSearch : 7.6.2

![image-20200623232452983](https://user-images.githubusercontent.com/60699771/85418002-3e734c00-b5ab-11ea-9cb7-c1064c931bc8.png)





## System Architecture

![image-20200623231717759](https://user-images.githubusercontent.com/60699771/85418042-47fcb400-b5ab-11ea-91f8-cafe10f3b9f0.png)





## 프로젝트 시 고민했었던 점

* 스크래이핑 성능 개선을 위한 병렬성 과 동시성 프로그래밍
  ![image-20200623233223098](https://user-images.githubusercontent.com/60699771/85418055-4b903b00-b5ab-11ea-9746-0d1c732e80e0.png)

* 구글 이미지 다운로드 시, 무작위 크롤링을 막고자 base64로 암호화된 이미지 복호화 필요

  ![image-20200623233440760](https://user-images.githubusercontent.com/60699771/85418062-4d59fe80-b5ab-11ea-9bd1-9bbd986f8f5e.png)

* 다음 뉴스 스크래이핑 시, 수천개의 페이지 수집으로 포털 사이트로부터 Connection 끊김 방지 필요

  * Fake-Agent 사용 
  * referer 사용
  * download delay 설정
  
* Scrapy 프레임워크와 Django 프레임워크 간 연동

  ![image-20200623233726319](https://user-images.githubusercontent.com/60699771/85418074-50ed8580-b5ab-11ea-8562-8b29ac5e11ce.png)





## TODO

* 수집한 뉴스 정보들을 NLP를 사용해 주제와 핵심 내용을 추려내 ElasticSearch 분석과 Kibana 시각화에 활용 필요