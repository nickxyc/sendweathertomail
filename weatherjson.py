import json
import requests
def get_weather():
    url = 'https://www.sojson.com/open/api/weather/json.shtml?city=芜湖'
    r = requests.get(url)
    r = json.loads(r.text)
    date = r['data']['forecast'][0]['date']
    sunrise = r['data']['forecast'][0]['sunrise']
    high = r['data']['forecast'][0]['high']
    low = r['data']['forecast'][0]['low']
    sunset = r['data']['forecast'][0]['sunset']
    aqi = r['data']['forecast'][0]['aqi']
    fx = r['data']['forecast'][0]['fx']
    fl = r['data']['forecast'][0]['fl']
    type = r['data']['forecast'][0]['type']
    notice = r['data']['forecast'][0]['notice']
    shidu = r['data']['shidu']
    pm25 = r['data']['pm25']
    pm10 = r['data']['pm10']
    quality = r['data']['quality']
    wendu = r['data']['wendu']
    ganmao = r['data']['ganmao']

    text = '这是XuYunchao先生开发的自动脚本，旨在向指定人发送当地天气，实验阶段请勿回复\n'\
        '今天是%s，天气为%s，现在的气温是%s℃，今天最高的气温是%s，最低气温是%s。aqi是%s。太阳在%s升起，%s落下。风向%s，风力%s，'\
            '湿度为%s，感冒情况%s，%s' \
           %(date,type,wendu,high,low,aqi,sunrise,sunset,fx,fl,shidu,ganmao,notice)
    return text