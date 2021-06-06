import json
import os
import random
import time

import requests
from bs4 import BeautifulSoup

from firebase import init_firebase, updateData

base_url = 'https://movie.naver.com/movie/point/af/list.nhn?&page={}'

init_firebase()


def main():
    for idx in range(1, 1001):
        print(f'Page #{idx}')
        url = base_url.format(idx)
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            trs = soup.select('table.list_netizen tbody tr')
            for tr in trs:
                # 평점 번호
                id = tr.find(class_='ac num').text
                title = tr.find(class_='title')
                # 감상평
                document = title.select_one('br').next_sibling.strip()
                # 평점
                score = title.select_one('div.list_netizen_score em').text
                # 이미 해당 id 를 가진 리뷰를 크롤링 했으면 종료한다.
                if os.path.exists(f'./jsons/{id}.json'):
                    print(f'{id} is already crawled.')
                    continue
                with open(f'./jsons/{id}.json', 'w', encoding='utf-8') as f:
                    print(f'{id} has been successfully crawled.')
                    data = {'document': document, 'score': int(score)}
                    updateData(id, data)
                    json.dump(data, f, ensure_ascii=False, indent=2)
        else:
            raise NotImplementedError
        # 1 ~ 10 초 사이 랜덤한 시간 만큼 멈춘다 -> 너무 빠르게 하면 block 가능성이 있습니다.
        time.sleep(random.uniform(1.0, 10.0))


if __name__ == '__main__':
    main()
