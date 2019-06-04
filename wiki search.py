import requests
from bs4 import BeautifulSoup
search_again="y"
while search_again!="n": #begin loop
  search=input("Welcome to wikipedia. What are you searching?\n") #ask user
  website=requests.get("https://en.wikipedia.org/wiki/"+search) #search
  website_content=website.content #take content
  website2=BeautifulSoup(website_content,features="html.parser") #parse

  title_num=website2.find_all('span', attrs={'class':'tocnumber'}) #get titles num for the searched item
  title_name=website2.find_all('span', attrs={'class':'toctext'}) # get names too

  for num,name in zip(title_num,title_name):
    if str(name.text)=="See also": #write all title names until it sees "See also"
      break
    print(num.text+" "+name.text)

  paragraphs = website2.find_all("p", attrs={'class':''}) #paragraphs in page
  if str(paragraphs[0].text).strip()=="Other reasons this message may be displayed:": #if no result is found
    print("Couldn't find result. Please give proper search name")
    continue #begin loop from start again
  print(paragraphs[0].text) #print first paragraph

  more=input("Would you like to read more? y/n\n")
  while more!="n":
    if more=="y":
      for all in paragraphs: #print all paragraphs
        print(all.text)
      break 
    else: #if input is neither y or n
      more=input("Invalid answer.\n")
  search_again=input("Do you want to search another item? y/n \n")
  while search_again!="n" and search_again!="y":
    search_again=input("Invalid answer.\n")
  if search_again=="n":
    break
