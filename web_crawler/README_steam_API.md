# Get All  STEAM User ID and Game Info

## STEAM Web API

Official Site Web API Doc Index: http://steamcommunity.com/dev

Detail: http://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_.28v0001.29

Well API description: https://wiki.teamfortress.com/wiki/WebAPI and http://steamwebapi.azurewebsites.net/

 3rd Doc about Web API: http://steamwebapi.azurewebsites.net/

- You are limited to one hundred thousand (100,000) calls to the Steam Web API per day. Valve may approve higher daily call limits if you adhere to these API Terms of Use.

--

STEAM API Key:


http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=
{}&steamids=76561197960435530

e.g:

http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={}&steamid=76561197961609023&format=json

json:  {"appid": 10,"playtime_forever": 32}

 ## Game

### Brief

 **Official Source**

 *GET*  the appid and title
[https://api.steampowered.com/ISteamApps/GetAppList/v2/](https://steamcommunity.com/linkfilter/https://api.steampowered.com/ISteamApps/GetAppList/v2/)

Date: 04/07/2017

Sum: 39482(04/07)-> 39513(04/10)

----

**Other data source**

Data Source: https://steamdb.info/tags/
Date: 04/07/2017
Sum: **149506**

Files: game-tag-sum.txt , game-tag-num.lst

--

Data Source: https://steamdb.info/apps/

Date: 04/07/2017

Sum:  760 x 75/page = 57000, 2 years updated game, it can be believed is the all game data.

!!!!!!! I think the data is more better. because past over 2 years, the old datas is not fit to recommendation system.

--

Data source: https://steamdb.info/instantsearch/

Date: 04/07/2017

Sum: 43897

--

Steamdb Apps list

https://steamdb.info/instantsearch/?q=&hPP=20&idx=steamdb&p=0&is_v=1

Total: 64286

--

There are a large different on sum;

**Maybe there are some game's old version(series version, such GTA1,2,3,4,5 ) **

So，crawl all app id informantion, then compare and get rid of duplicate item to get the last list;



### Detail

Get the game detail from the http://store.steampowered.com/api/appdetails?appids=<app_id>

e.g.: http://store.steampowered.com/api/appdetails?appids=221540

The request will return false or be forbidden after about 200 request / each



## User

We need Steam ID, basic info, player rating and friend list. While there are no any api what can get all user data from STEAM. So, construct some id according to the STEAM ID Format.

Steam ID can split **<u>2</u>** parts, **the fixed + 10 bits** serial number.

e.g. **7656119** + **##########**  (# => [0-9]), so we will get 100 Million ID. The get rid of  all IDS what we have validated(about **275120** )

** 经过大量分段测试，发现， 最可能的ID范围 在 1-800268502 之间**



####Validating User ID####

Official site provide a profile url,  it can be used to check the ID, if profile page is ok, then id is valid.

http://steamcommunity.com/profiles/<ID>
e.g: http://steamcommunity.com/profiles/76561197960265738



-----3rd-----

https://steamdb.info/calculator/76561197960265738/

https://steamid.io/lookup/76561197960265700

http://steamidfinder.com/lookup/76561197960265700/

**Validate Steam ID by 3rd API to valid ban our IP by STEAM**

e.g.:

76561197960265700 — unavailable

76561197960265738 — OK

76561197960265740 -- private
76561197960265729
**76561197960265728** — is the first id in steam id seres



### Rating

Under the user profile, the all games info can be gotten on http://steamcommunity.com/profiles/76561198040934972/games?tab=all&xml=1  maybe can change to json, but directly change to json=1, not work;

while, in the whole page, there is a json string in script scetion

get all game from api:

http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=7BA13DD5D9CD290F7450FA29F09D0F39&steamid=76561197960434622&format=json

-steam will ban all  exceeded limit ip and high frequency ip



----

- reference: http://store.steampowered.com/stats/
- steam id finder: http://steamidfinder.com/lookup/76561197960265700/
- steam spy: https://steamspy.com/
- steam db: https://steamdb.info/tags/
- steamworks: https://partner.steamgames.com/documentation/api
