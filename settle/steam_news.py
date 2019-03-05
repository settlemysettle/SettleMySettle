import json
import urllib.parse
import urllib.request

# might need to read key

def get_news(steamID, count=5):
    root_url = ""
    searchUrl = "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid={steamID}&count={count}".format(steamID=steamID, count=count)
    print(searchUrl)

    results = []
    try:
        response = urllib.request.urlopen(searchUrl).read().decode('utf-8')
        json_response = json.loads(response)
        
        for post in json_response["appnews"]["newsitems"]:
            # look at all of the possible
            results.append({'title': post['title'].replace(" s ", "'s "),
                            'link': post['url'],
                            'summary': post['contents'][:300],
                            'appid': post['appid']})

    except Exception as e:
        print("Problem querying Steam API", e)

    return results
        


# get_news(289070, 5)