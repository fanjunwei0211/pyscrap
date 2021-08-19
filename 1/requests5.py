import json
import requests

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    address = input('餐厅地址   ')
    data = {
        'cname': '',
        'pid': '',
        'keyword': address,
        'pageIndex': '1',
        'pageSize': '10',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36'
    }

    response = requests.post(url=url, data=data, headers=headers)
    print(response.text)
    list_data = response.json()

    fp = open('douban_name.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)

    print("Done!")
