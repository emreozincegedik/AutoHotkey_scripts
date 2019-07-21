import requests
from bs4 import BeautifulSoup
proper=""
while True:
  name=input("Please give "+proper+"name of the movie: ")
  r=requests.get("https://1337x.to/search/"+name)
  html =r.content
  parsed_html=BeautifulSoup(html,features="html.parser")
  print(parsed_html)

"""   results=parsed_html.find_all('tr')
  print(results.text) """