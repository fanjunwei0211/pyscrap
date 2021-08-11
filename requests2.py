import requests

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36'
    }

    url = "https://www.sogou.com/web"
    kw = input('Enter a word')
    param = {
        'query': kw
    }
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    print(page_text)

    with open('./sougou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print("Done!")
