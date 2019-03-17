import json
import urllib.parse
import urllib.request
import re
from html2text import html2text

def get_news(steamID, count=5):
    root_url = ""
    searchUrl = "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid={steamID}&count={count}&feeds=steam_community_announcements".format(steamID=steamID, count=count)

    results = []
    try:
        response = urllib.request.urlopen(searchUrl).read().decode('utf-8')
        json_response = json.loads(response)
        
        for post in json_response["appnews"]["newsitems"]:
            # look at all of the possible
            content = post['contents'][:1000]
            newsImage = getImage(content)
            content = trimContent(html2text(content))[:200] + "..."
            results.append({'title': post['title'].replace(" s ", "'s "),
                            'link': post['url'],
                            'summary': content,
                            'feedlabel': post['feedlabel'],
                            'author': post['author']})
    except Exception as e:
        print("Problem querying Steam API:", e)

    return results
        

def getImage(content):
    try:
        newsImage = re.findall(r'(?:src=\"|\[img\])(.*?)(?:"|\[\/img\])', content)[0]
        return newsImage
    except Exception as ex:
        return "noImg"

def trimContent(content):
    for match in re.finditer(".*? ", content):
        span = match.span()
        group = match.group()
        if (content[span[0]].isalpha()):
            break
    
    return content[span[0]:]
