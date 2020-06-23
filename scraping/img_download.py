import os
import base64
import requests
import shutil
from scraping.img_url_collect import ImageURLCollect
from functools import partial
from multiprocessing import Pool, Process, Queue


class ImageScraper:
    def __init__(self, n_threads, google, naver, download_path):
        self.n_threads = n_threads
        self.google = google
        self.naver = naver
        self.download_path = download_path


    def make_dir(self, keyword):
        """
        파일 폴더 만들기
        """
        print("Create folder name : {}/{}".format(self.download_path, keyword))
        current_path = os.getcwd()
        path = os.path.join(current_path, self.download_path+"/" + keyword)
        print(path)
        try:
            if not os.path.exists(path):
                os.makedirs(path)
                
        except OSError as e:
            print("folder creation failed!")
            print("Create folder name : {}/{}".format(self.download_path, keyword))

            # 런타임 에러 raise
            raise RuntimeError('System Exit!')

        else:
            print('folder is created!')


    def get_keywords(self, keywords_file='keywords.txt'):
        with open(keywords_file, 'r', encoding='utf-8') as f:
            contents = f.read()
            lines = contents.split('\n')
            lines = filter(lambda x: x != '' and x is not None, lines)
            keywords = sorted(set(lines))

        print(f'{len(keywords)} keywords found : {keywords}')

        with open(keywords_file, 'w+', encoding='utf-8') as f:
            for keyword in keywords:
                f.write(f'{keyword}\n')

        return keywords


    def scraping_start(self):
        keywords = self.get_keywords()
        tasks = []

        print('Image Search Start')

        for keyword in keywords:
            if self.google:
                tasks.append([keyword, 'google'])
            if self.naver:
                tasks.append([keyword, 'naver'])
            self.make_dir(keyword)

        pool = Pool(self.n_threads)
        pool.map_async(self.site_mapping, tasks)
        pool.close()
        pool.join()
        print('Task ended. Pool join.')
        print('End Program')

    def site_mapping(self, args):
        self.download_from_site(keyword=args[0], site=args[1])

    def download_from_site(self, keyword, site):
        # 1. 크롬 드라이버 start
        try:
            image_URLs = ImageURLCollect()
        except Exception as e:
            print('Error occurred while initializing chromedriver - {}'.format(e))
            return

        # 2. 크롬 드라이버를 통한 이미지 search
        try:
            print('링크 수집 시작 검색어 : {}, 검색 사이트 : {}'.format(keyword, site))

            if site == "google":
                links = image_URLs.google_search(keyword)
            elif site == "naver":
                links = image_URLs.naver_search(keyword)
            else:
                print("검색 사이트를 확인해주세요(google and naver only")
                links = []

            print('Downloading images from collected links... {} from {}'.format(keyword, site))
            self.download(keyword, links, site)

            print('Done {} : {}'.format(site, keyword))

        except Exception as e:
            print('Exception {}:{} - {}'.format(site, keyword, e))

    def download(self, keyword, links, site):
        '''
        수집 URL을 통한 이미지 파일 다운로드
        '''
        total = len(links)

        for index, link in enumerate(links):
            try:
                print('Downloading {} from {}: {} / {}'.format(keyword, site, index + 1, total))

                if str(link).startswith('data:image/jpeg;base64'):
                    response = self.base64_to_object(link)
                    ext = 'jpg'
                    is_base64 = True
                elif str(link).startswith('data:image/png;base64'):
                    response = self.base64_to_object(link)
                    ext = 'png'
                    is_base64 = True
                else:
                    response = requests.get(link, stream=True)
                    ext = self.get_extension_from_link(link)
                    is_base64 = False

                no_ext_path = '{}/{}/{}_{}'.format(self.download_path, keyword, site, str(index).zfill(4))
                path = no_ext_path + '.' + ext
                self.save_object_to_file(response, path, is_base64=is_base64)

                del response

            except Exception as e:
                print('Download failed - ', e)
                continue


        
        
    def base64_to_object(self, src):
        '''
        base64로 암호화된 구글 이미지 복호화
        '''
        print("decrypt image")
        header, encoded = str(src).split(',', 1)
        data = base64.decodebytes(bytes(encoded, encoding='utf-8'))

        return data



    def get_extension_from_link(self, link, default='jpg'):
        '''
        확장자 세팅
        '''
        splits = str(link).split('.')
        if len(splits) == 0:
            return default
        ext = splits[-1].lower()
        if ext == 'jpg' or ext == 'jpeg':
            return 'jpg'
        elif ext == 'gif':
            return 'gif'
        elif ext == 'png':
            return 'png'
        else:
            return default



    def save_object_to_file(self, object, file_path, is_base64=False):
        '''
        save image file
        '''
        
        try:
            with open('{}'.format(file_path), 'wb') as file:
                if is_base64:
                    file.write(object)
                else:
                    shutil.copyfileobj(object.raw, file)
        except Exception as e:
            print('Save failed - {}'.format(e))
        
            

if __name__ == '__main__':
    image_scraper = ImageScraper(4, True, True, "download")
    image_scraper.scraping_start()