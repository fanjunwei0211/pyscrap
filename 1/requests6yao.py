import requests
import json

if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text
    print(page_text)

    with open('huazhuangpin.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)