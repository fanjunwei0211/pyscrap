import requests
import json
import pandas
import time

#获取时间戳
t_param = time.time()
t_list = str(t_param).split('.')

headers = {
    'authority': 'rate.tmall.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '^\\^',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'script',
    'referer': '根据商品信息填写referer',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '你的cookie',
}

#一定要加动态参数！
params={
    "itemId":"根据url参数获取",
    "sellerId":"根据url参数获取",
    "currentPage":"1",
    "callback":str(int(t_list[1][3:])+1),
    "_ksTS":t_list[0]+t_list[1][:3]+"_"+t_list[1][3:]
}


col=['auctionSku','rateContent','rateDate','reply']
auctionSku=[]
rateContent=[]
rateDate=[]
reply=[]
pics=[]

url="https://rate.tmall.com/list_detail_rate.htm"

for page in range(1,100):
    params["currentPage"]=str(page)
    req=requests.get(url,params,headers=headers).content.decode('utf-8');
    result=json.loads(req[req.index('({')+1:-1]);
    for item in result['rateDetail']['rateList']:
        auctionSku.append(item['auctionSku'])
        rateContent.append(item['rateContent'])
        rateDate.append(item['rateDate'])
        pics.append(item['pics'])
        if item['appendComment']:
            reply.append(item['appendComment']['content'])
        else:
            reply.append('')
    print('第'+str(page)+'页完毕')
    time.sleep(8)

df = pandas.DataFrame({
    '产品名字':auctionSku,
    '初评':rateContent,
    '初评时间':rateDate,
    '初评图片':pics,
    '追评':reply
})

df.to_excel("1-99.xlsx", sheet_name="评论数据", index=False, header=True)
