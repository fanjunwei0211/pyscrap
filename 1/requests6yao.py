import requests
import json

if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    # 批量获取id
    data = {
        'on': 'true',
        'page': '1',
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'lambda ': '',
        'applysn': ',',

    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36'
    }

    id_list = []  # 企业id
    all_data_list = []  # 企业详情数据
    page_json = requests.post(url=url, headers=headers, data=data).json()
    for dic in page_json['list']:
        id_list.append(dic['ID'])
    print(id_list)

    # 获取数据详情页
    detail_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        detail_data = {
            'id': id,
        }
        detail_json = requests.post(url=detail_url, headers=headers, data=detail_data).json()
        # print(detail_json, '---------------------end-----------------------')
        all_data_list.append(detail_json)

    fp = open('allData.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
    print('Done!')
