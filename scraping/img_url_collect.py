from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from urllib import parse
from bs4 import BeautifulSoup
import os


class ImageURLCollect():

    def __init__(self):
        """
        크롬 브라우저 실행 및 윈도우 사이즈 조절, download 경로 초기화
        """
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # webdriver Headless 모드
        # self.browser = webdriver.Chrome(os.path.dirname(os.path.abspath( __file__ ))+'/webdriver/chrome/chromedriver.exe', options=chrome_options)
        # webdriver 일반모드
        self.browser = webdriver.Chrome(os.path.dirname(os.path.abspath( __file__ ))+'/webdriver/chrome/chromedriver.exe')
        self.browser.implicitly_wait(2)
        self.browser.maximize_window()

    def wait_and_click(self, xpath):
        """
        WebDriver를 통해 이미지 검색 중 "더 보기" 버튼 클릭 기능 수행
        """
        try:
            elem = WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            elem.click()
            self.highlight(elem)
        except Exception as e:
            print('Click time out - {}'.format(xpath))
            print('Refreshing browser...')
            self.browser.refresh()
            time.sleep(2)
            return self.wait_and_click(xpath)
        return elem

    def highlight(self, element):
        """
        더보기 입력 후 스크롤 page down 수행
        """
        self.browser.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, "background: yellow; border: 2px solid red;")


    def remove_duplicates(self, _list):
        """
        중복 이미지 제거
        """
        return list(dict.fromkeys(_list))


    def google_search(self, keyword):
        parse_keyword = parse.quote_plus(keyword)
        self.browser.get("https://www.google.com/search?q={}&source=lnms&tbm=isch".format(parse_keyword))
        time.sleep(1)

        elem = self.browser.find_element_by_tag_name("body")
        for i in range(50):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)

        try:
            self.wait_and_click('//input[@type="button"]')            
            for i in range(50):
                elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.2)                
        except ElementNotVisibleException as e:
            pass

        links = self.google_image_url_collect(keyword)
        return links


    def google_image_url_collect(self, keyword):
        '''
        이미지 다운로드를 위한 html 내 이미지 URL 검색 및 수집
        '''
        # html내 이미지 주소만 수집
        soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        img_lists = soup.select('div.bRMDJf.islir')

        print('Collecting Image URL on Google')

        links = []

        for img in img_lists:
            try:
                # self.highlight(img)
                src = img.select_one("img")['src']

                # Google seems to preload 20 images as base64
                if str(src).startswith('data:'):
                    src = img.select_one("data-iurl")
                links.append(src)

            except Exception as e:
                print('[Exception occurred while collecting links from google] {}'.format(e))

        # print(links)
        links = self.remove_duplicates(links)

        print('링크 수집 결과: 사이트: {}, 검색어: {}, 다운 총개수: {}'.format('google', keyword, len(links)))       
        self.browser.close()

        return links

    def naver_search(self, keyword):
        parse_keyword = parse.quote_plus(keyword)
        self.browser.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}".format(parse_keyword))      
        time.sleep(1)

        elem = self.browser.find_element_by_tag_name("body")
        for i in range(50):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)

        try:
            self.wait_and_click('//a[@class="btn_more _more"]')            
            for i in range(50):
                elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.2)                
        except ElementNotVisibleException as e:
            pass

        links = self.naver_image_url_collect(keyword)
        return links


    def naver_image_url_collect(self, keyword):
        '''
        이미지 다운로드를 위한 html 내 이미지 URL 검색 및 수집
        '''
        # html내 이미지 주소만 수집
        soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        img_lists = soup.select('div.img_area._item')

        print('Collecting Image URL On Naver')

        links = []
        missing = []
        for img in img_lists:
            try:
                # self.highlight(img)
                src = img.select_one('a > img')['src']
                if src[0] != 'd':
                    links.append(src)
                elif src[0] == 'd':
                    missing.append(src)

            except Exception as e:
                print('[Exception occurred while collecting links from google] {}'.format(e))

        print("base64 암호화에 따른 다운로드 불가 개수 : {}".format(len(missing)))
        links = self.remove_duplicates(links)

        print('링크 수집 결과: 사이트: {}, 검색어: {}, 다운 총개수: {}'.format('naver', keyword, len(links)))       
        self.browser.close()

        return links
            

if __name__ == '__main__':
    image_URL = ImageURLCollect()
    links = image_URL.google_search("아이린")
    image_URL = ImageURLCollect()
    links = image_URL.naver_search("김민아")