import json
import requests

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/search_subjects'
    start_t = input('第几部电影   ')
    param = {
        'type': 'movie',
        'tag': '喜剧',
        'sort': 'recommend',
        'page_limit': '20',
        'page_start': start_t
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36'
    }
    response = requests.get(url=url, param=param, headers=headers)
    list_data = response.json()

    fp = open('douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)

    print("Done!")
