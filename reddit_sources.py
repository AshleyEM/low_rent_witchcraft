from bs4 import BeautifulSoup as bs
import urllib.request
import random

# notation: 
#      A >> B  = take B out of A
#     A -> B = put A into B

def get_response(url):
    masks = [
        {"user-agent":"Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"},
        {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"},
        {"user-agent":"Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"},
        {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"}
    ]
    req = urllib.request.Request(url, headers=random.choice(masks))
    return urllib.request.urlopen(req) # response >> html

#  given "https://www.site.com/whatever/"  
#  return  "www.site.com"
def get_domain(url):
    splitted = url.split('/')
    if 'http' in splitted[0]:
        return splitted[2]

# SUBREDDIT FRONT PAGE >> COMMENTS >> EXTERNAL SOURCES
# returns dictionary of urls outside of reddit and their count
# yes I'm aware the time complexity of this is O(dumb)
def subreddit_srcs(subr): # input "subreddit" without "r/"
    sources = {}
    req = get_response("https://old.reddit.com/r/" + subr) # send http request
    html = bs(req.read(), 'html.parser') # response >> html
    for a in html.find_all('a', class_="bylink comments may-blank", href=True): # html >> <a>
        req2 = get_response(a['href']) # <a> ~~> comments page
        html2 = bs(req2.read(), 'html.parser') # response >> html
        for a2 in html2.html.find_all('a', href=True):
            src = get_domain(a2['href']) # https://www.src.com/whatever/ >> www.src.com
            if src != None and 'reddit' not in a2['href'] and 'redd.it' not in a2['href']:
                if src not in sources: 
                    sources[src] = 1   # www.src.com  +1 -> {}
                else:
                    sources[src] += 1
    return sources


print(subreddit_srcs('all'))
