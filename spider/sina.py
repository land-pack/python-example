import requests


url = 'https://weibo.com/p/1005056094495150/follow?relate=fans&from=100505&wvr=6&mod=headfans&current=fans#place'

url = 'https://weibo.com/u/6094495150?is_hot=1'

r = requests.get(url)

print(r.content)

