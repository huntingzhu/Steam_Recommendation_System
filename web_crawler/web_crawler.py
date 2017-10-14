import sys
import requests
import json

from bs4 import BeautifulSoup as bs
from contextlib import closing
import urllib
import re


def get_user_id(user_profile, user_ids):
    url = user_profile
    with closing(urllib.urlopen(url)) as page:
        for line in page:
            if "steamid" in line:
                try:
                    user_id = re.search("\"steamid\":\"(\d+)\"", line).group(1)
                    # print user_id + ' ' + user_profile
                    if user_id != None:
                        user_ids.append(user_id)
                        break
                except:
                    continue

def get_online_users(member_list_no, user_ids):
    url = 'https://steamcommunity.com/games/steam/members?p=' + str(member_list_no)
    resp = requests.get(url)
    soup = bs(resp.text, 'html.parser')
    # print(soup.prettify())
    # search profile of users who are online/in-game
    all_users = soup.find_all("div", \
                              onclick = re.compile("top\.location\.href='https:\/\/steamcommunity\.com\/id\/(\w+)'"), \
                              class_ = re.compile("online|in-game"))
    # get user names
    for user in all_users:
        user_profile = user.div.div.div.a['href'].encode("ascii")
        # print user_profile
        get_user_id(user_profile, user_ids)

def dump_user_id(user_ids, user_out_file):
    with open(user_out_file, 'w') as f:
        for idx in range(0, len(user_ids)):
            user_id_idx = {'user_idx': idx, 'user_id': user_ids[idx]}
            json.dump(user_id_idx, f)
            f.write('\n')

# dump player summaries
def process_json_obj(resp, user_out_file, user_id):
    if 'user_summary' in user_out_file:
        # corner case: list index out of range
        try:
            obj = resp.json()['response']['players'][0]
        except:
            obj = {'steamid' : user_id}
    elif 'user_owned_games' in user_out_file:
        obj = resp.json()['response']
        obj = {'steamid' : user_id, 'game_count' : obj['game_count'], 'games' : obj['games']}
    elif 'user_friend_list' in user_out_file:
        obj = resp.json()['friendslist']
        obj = {'steamid' : user_id, 'friends' : obj['friends']}
    elif 'user_recently_played_games' in user_out_file:
        obj = resp.json()['response']
        try:
            obj = {'steamid' : user_id, 'total_count' : obj['total_count'], 'games' : obj['games']}
        except:
            # corner case: total_count is zero
            obj = {'steamid' : user_id, 'total_count' : obj['total_count'], 'games' : []}
    return obj

def dump_user_info(url, user_ids, user_out_file):
    with open(user_out_file, 'w') as f:
        for user_id in user_ids:
            url_temp = url + str(user_id)
            resp = requests.get(url_temp)
            # resp = requests.head(url_temp)
            obj = process_json_obj(resp, user_out_file, user_id)
            json.dump(obj, f)
            f.write('\n')


if __name__ == '__main__':
    member_list_page_no = 5
    key = '0D37BB1ABB4C0AFAF76379F37EDB4C8D'

    user_ids = []
    for idx in range(1, member_list_page_no + 1):
        print "Member List " + str(idx)
        get_online_users(idx, user_ids)
        print "Total online users found:"
        print len(user_ids)

    # dump user id
    dump_user_id(user_ids, 'data/user_idx_sample.json')


    # dump player summaries
    url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + key + '&steamids='
    dump_user_info(url, user_ids, 'data/user_summary_sample.json')

    # dump owned games
    url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=' + key + '&steamid='
    dump_user_info(url, user_ids, 'data/user_owned_games_sample.json')

    # dump friendList
    url = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=' + key + '&steamid='
    dump_user_info(url, user_ids, 'data/user_friend_list_sample.json')

    # dump recently Played games
    url = 'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=' + key + '&steamid='
    dump_user_info(url, user_ids, 'data/user_recently_played_games_sample.json')
