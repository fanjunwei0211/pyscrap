import requests
import re


def getHTMLText(url):  # 获得页面函数
    try:
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
            'cookie': "cna=DHOaGVOTdD4CAbfPBPBTZWm/; lgc=%5Cu6C90%5Cu5E74%5Cu706C%5Cu6728%5Cu5893; tracknick=%5Cu6C90%5Cu5E74%5Cu706C%5Cu6728%5Cu5893; thw=cn; enc=0JGU5%2FKpkQG9H6Z15veZ%2Bu0oVqpcAQc8hkwAG9t6K%2FIjq1p2svJ22S6afRQ%2F5mrs4Jz3r3Ukl02HT2QvmY1FxQ%3D%3D; _m_h5_tk=8a6547a4a85582fa0417ec7b15f5ad9a_1633072188933; _m_h5_tk_enc=ec14a13dfd4989512a4e556b6553560b; t=0d3d9b2589db76201478bad573278804; _tb_token_=e977531e83137; cookie2=18e3e357ea639906c02764ae2cfea1d7; _samesite_flag_=true; cancelledSubSites=empty; dnk=%5Cu6C90%5Cu5E74%5Cu706C%5Cu6728%5Cu5893; _cc_=URm48syIZQ%3D%3D; sgcookie=E100p85K4IhaFDxg7M0PPmFCqWx70ddRhDxQWDQnHnI4FhobfFbDkMDRPVlFubjagfyrnjsaVu5JaMDkWBzlR6oFzYk%2FAfIyMrMSng8z3cIvyzQ%3D; uc3=lg2=VFC%2FuZ9ayeYq2g%3D%3D&vt3=F8dCujaNo3CzyZg6ejg%3D&nk2=gIdYVPyZFz1gqA%3D%3D&id2=VyyUw9BPjgHPTQ%3D%3D; csg=5423233a; skt=401cd57822d44497; existShop=MTYzMzA2MzkxNw%3D%3D; uc4=nk4=0%40gsxc7D7%2B%2FIsZlBPFX4fIa1apcX4L&id4=0%40VXtbaq2Ipq%2Bq0lNh43gNKrahCQPe; mt=ci=28_1; _uab_collina=163307511405288333757749; x5sec=7b227365617263686170703b32223a226333393432613466323066373964656662616666303039623932633739336631434b6a2f326f6f47454f6e387a6f37473470484139414561444451774e5467314d4449334f5463374d54436e68594b652f502f2f2f2f3842227d; uc1=pas=0&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=URm48syIYB3rzvI4Dim4&existShop=false&cart_m=0&cookie14=Uoe3dP2Yspnu4A%3D%3D; JSESSIONID=BBB89A3127B894F9FB6E5C123EF83F89; l=eBM0AtjuO19QtJGoBOfwourza77OSIRAguPzaNbMiOCP_xCp5ddlW6ePUZ89C3GVh6JJR3ukFkxYBeYBqIv4n5U62j-la_kmn; isg=BHd3G-RS2hjVf2Cxv9IPQFb_BmvBPEueb_KD3ckkk8ateJe60Qzb7jVaWtgmkCMW"
        }
        r = requests.get(url, headers=header, timeout=300)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):  # 解析获得的页面
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)  # 最小匹配
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])  # 将plt的第i个元素取出，利用:划分为列表,取出第二个元素，获得:后面的有效信息
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])  # 一个元素中有两个值,二维列表
    except:
        print("")


def printGoodlist(ilt):  # 输出结果信息到屏幕
    tplt = "{:4}\t{:8}\t{:16}"  # \t缩进
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():  # 主函数
    goods = input("请输入要爬取的商品:")
    depth = eval(input("请输入爬取页数:"))  # 爬取深度
    start_url = 'https://s.taobao.com/search?q=' + goods
    indolist = []  # 输出结果
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            # with open(f"./taobao/{i}.html", mode='w', encoding='utf-8') as f:
            #     f.write(html)
            parsePage(indolist, html)
        except:
            continue
    printGoodlist(indolist)


main()
