from requests_html import AsyncHTMLSession
asession = AsyncHTMLSession()

async def get_pythonorg():
    r = await asession.get('https://python.org/')

async def get_reddit():
   r = await asession.get('https://reddit.com/')

async def get_google():
    r = await asession.get('https://google.com/')

asession.run(get_pythonorg, get_reddit, get_google)

print(r.html.links)