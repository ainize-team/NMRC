import gc
import os
import random
import time

import requests
from bs4 import BeautifulSoup

from firebase import init_firebase, update_data

base_url = 'https://movie.naver.com/movie/point/af/list.nhn?&page={}'

# 전체 크롤링 수집 주기 ( 7day )
TIME_GAP = 60 * 60 * 24 * 7


def main():
    init_firebase()
    while True:
        for idx in range(1000, 0, -1):
            print(f'Page #{idx}')
            url = base_url.format(idx)
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                trs = soup.select('table.list_netizen tbody tr')
                for tr in trs:
                    # 평점 번호
                    document_id = tr.find(class_='ac num').text
                    title = tr.find(class_='title')
                    # 감상평
                    document = title.select_one('br').next_sibling.strip()
                    # 평점
                    score = title.select_one('div.list_netizen_score em').text
                    # 이미 해당 id 를 가진 리뷰를 크롤링 했으면 종료한다.
                    if os.path.exists(f'./jsons/{document_id}.json'):
                        print(f'{document_id} is already crawled.')
                        continue
                    data = {'document': document, 'score': int(score)}
                    update_data(document_id, data)
                # 1 ~ 10 초 사이 랜덤한 시간 만큼 멈춘다 -> 너무 빠르게 하면 block 가능성이 있습니다.
                time.sleep(random.uniform(1.0, 10.0))
            else:
                raise NotImplementedError
        # 1시간 정도 기다리기 ( 데이터는 계속 모이기 때문 )
        time.sleep(TIME_GAP)
        gc.collect()
    pass


if __name__ == '__main__':
    main()
