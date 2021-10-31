# -*- coding: utf-8 -*-
# @Time : 2021/5/12 17:07
# @Author : Leviathan_Sei
# @File : get_item_id.py
# @Python : 3.7

import requests
import time
import csv
import re


def get_id_html(store, page):
    base_url = "https://{}.tmall.com/i/asynSearch.htm?_ksTS=1618216498569_351&callback=jsonp352&mid=w-23295354947-0&wid=23295354947&path=/category.htm&spm=a1z10.1-b-s.w5001-23295377977.6.2059782don1Eg5&search=y&orderType=hotsell_desc&scene=taobao_shop&pageNo={}"
    url = base_url.format(store, page)
    cookies = {
        "Cookies": "lid=%E6%B2%90%E5%B9%B4%E7%81%AC%E6%9C%A8%E5%A2%93; enc=0JGU5%2FKpkQG9H6Z15veZ%2Bu0oVqpcAQc8hkwAG9t6K%2FIjq1p2svJ22S6afRQ%2F5mrs4Jz3r3Ukl02HT2QvmY1FxQ%3D%3D; cna=+lG/GZ6bGmQCAd7Rmz3Cq3vL; _m_h5_tk=2010134a863f0f82ce18e091db35f08f_1633024572965; _m_h5_tk_enc=bb8e61f07def631da54e0ecfe92eadf8; dnk=%5Cu6C90%5Cu5E74%5Cu706C%5Cu6728%5Cu5893; uc1=pas=0&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=false&cookie14=Uoe3dP2ZQt10Jw%3D%3D&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie21=WqG3DMC9Fb5mPLIQo9kR&cart_m=0; uc3=lg2=VFC%2FuZ9ayeYq2g%3D%3D&vt3=F8dCujaNo3CzyZg6ejg%3D&nk2=gIdYVPyZFz1gqA%3D%3D&id2=VyyUw9BPjgHPTQ%3D%3D; tracknick=%5Cu6C90%5Cu5E74%5Cu706C%5Cu6728%5Cu5893; _l_g_=Ug%3D%3D; uc4=nk4=0%40gsxc7D7%2B%2FIsZlBPFX4fIa1apcX4L&id4=0%40VXtbaq2Ipq%2Bq0lNh43gNKrahCQPe; unb=4058502797; lgc=%5Cu6C90%5Cu5E74%5Cu706C%5Cu6728%5Cu5893; cookie1=VAdfYoz4PAReykvEBPbo8YH5m5R4qIUWZ52QtKACA5s%3D; login=true; cookie17=VyyUw9BPjgHPTQ%3D%3D; cookie2=18e3e357ea639906c02764ae2cfea1d7; _nk_=%5Cu6C90%5Cu5E74%5Cu706C%5Cu6728%5Cu5893; sgcookie=E100p85K4IhaFDxg7M0PPmFCqWx70ddRhDxQWDQnHnI4FhobfFbDkMDRPVlFubjagfyrnjsaVu5JaMDkWBzlR6oFzYk%2FAfIyMrMSng8z3cIvyzQ%3D; cancelledSubSites=empty; t=0d3d9b2589db76201478bad573278804; sg=%E5%A2%937d; csg=5423233a; _tb_token_=e977531e83137; pnm_cku822=; l=eBS8Nk8VOhG0qWaXKOfwourza77OSIRAguPzaNbMiOCP_z5p5ZLlW6eyiIY9C3GVh6opR3ukFkxYBeYBqnv75O95iLq_DoHmn; isg=BK-vdjMSEnAYlihM4rGk4r3JPsO5VAN210pLpcE8S54kEM8SySSTxq3GkgAuaNvu"
    }
    headers = {
        "Host": str(store) + ".tmall.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }
    response = requests.get(url, cookies=cookies, headers=headers).text
    time.sleep(5)
    return response


store = "chaopaishuma"

for page in range(1, 100):
    print("开始爬取第" + str(page) + "页")
    html = get_id_html(store, page)
    print("爬取完成")
    # 这一步的目的是清楚多余的空格
    html = re.sub('\s', '', str(html))
    item_data = {}

    # 这里使用正则表达式
    # 商品名
    data1 = re.findall('<imgalt=\\\\"(.*?)\\\\"', html)
    # 商品id
    data2 = re.findall('data-id=\\\\"(.*?)\\\\">', html)
    # 价格
    data3 = re.findall('c-price\\\\">(.*?)<', html)
    # 销量
    data4 = re.findall('sale-num\\\\">(.*?)<', html)
    # 评价
    data5 = re.findall('评价:(.*?)<', html)
    if len(data2) <= 22:
        print("该店铺数据爬取完毕！\n退出！")
        break
    # 索引从第一个到倒数第11个。
    for i in range(0, len(data2) - 10):
        item_data[data2[i]] = []
        # 名字
        item_data[data2[i]].append(data1[i])
        # id
        item_data[data2[i]].append(data2[i])
        # 现价
        item_data[data2[i]].append(data3[i])
        # 总销售量
        item_data[data2[i]].append(data4[i])
        # 评论数
        item_data[data2[i]].append(data5[i])
    print("开始保存")
    with open(store + 'data.csv', 'a', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        for k, v in item_data.items():
            print(v)
            w.writerow(v)
    print("第" + str(page) + "页保存完毕！")
