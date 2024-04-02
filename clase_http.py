import requests

dir_url='https://www.google.com/'
r=requests.get(url=dir_url)
print(r.text)