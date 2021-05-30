#Token price scraping

def obtain_price():
    ssl._create_default_https_context = ssl._create_unverified_context
    url = ''
    data = urllib.request.urlopen(url).read()
    jsonn = json.loads(data)
    price_token = jsonn[-1][1]
    return price_token