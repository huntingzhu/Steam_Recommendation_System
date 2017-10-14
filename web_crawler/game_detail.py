import sys
import requests
import json

from bs4 import BeautifulSoup as bs
from contextlib import closing
import urllib
import re
import time


def get_app_id_list():
    url = 'https://steamcommunity.com/linkfilter/https://api.steampowered.com/ISteamApps/GetAppList/v2/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'}
    resp = requests.get(url,header)

    app_id_objs = resp.json()['applist']['apps']
    app_id_list = []

    for app in app_id_objs:
        app_id_list.append(app['appid'])

    return app_id_list

def get_game_detail(app_id_list, num, game_detail_out_file):
    url = 'https://store.steampowered.com/api/appdetails?appids='
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'}
    with open(game_detail_out_file, 'w') as f:
        for idx in xrange(num):
            url_temp = url + str(app_id_list[idx])
            time.sleep(.100) # sleep 100ms
            resp = requests.get(url_temp, header)

            obj = resp.json()
            for key in obj:
                if obj[key]["success"] is True :
                    json.dump(obj[key]["data"], f)
                    f.write('\n')

if __name__ == '__main__':
    app_id_list = get_app_id_list()
    print "total apps: " + str(len(app_id_list))

    get_game_detail(app_id_list,10,"data/game_detail.json")
