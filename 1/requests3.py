import requests
import json

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36'
    }

    url = "https://fanyi.baidu.com/sug"
    kw_ = input('Enter a word')
    data = {
        'kw': kw_
    }
    response = requests.post(url=url, data=data, headers=headers)
    dic_obj = response.json()
    filename = kw_+'.json'
    print(dic_obj)
    fp = open(filename, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

    print("Done!")
