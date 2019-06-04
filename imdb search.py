import requests
from bs4 import BeautifulSoup
import re
import sys
proper=""
while True:  
  name=input("Please give "+proper+"name of the movie: ")
  r=requests.get("https://www.imdb.com/find?ref_=nv_sr_fn&q="+name+"&s=all")
  html =r.content
  parsed_html=BeautifulSoup(html,features="html.parser")

  movie_names= parsed_html.body.find('table', attrs={'class':'findList'})
  if movie_names==None:
    print("No such movie is found")
    proper="proper "
    continue
  regex=re.findall('\s{2,}(.*?\))',movie_names.text)
  movies=movie_names.find_all('td', attrs={'class':'result_text'})
  review_long_movies={}
  for movie,name in zip(movies,regex):
    link=movie.find('a').attrs['href']
    a=requests.get("https://www.imdb.com"+link)
    movie_page=a.content
    parsed_movie_page=BeautifulSoup(movie_page,features="html.parser")
    point=parsed_movie_page.body.find('div',attrs={'class':'ratingValue'})
    if point!=None:
      print("\n"+name.strip()+" "+point.text.strip())
    else:
      print("\n"+name.strip()+" No rating")
    commentdiv=parsed_movie_page.body.find('div',attrs={'class':'user-comments'})
    if commentdiv!=None:
      comment=commentdiv.find('p')
      if len(comment.text)>200:
        print(comment.text[:200]+"...")
        review_long_movies[name]=comment.text
      else:
        print(comment.text)
    else:
      print("No reviews exist")
    proper=""
  if len(review_long_movies)!=0:
    want_full=input("Do you want to see full review of a movie? y/n ")
    while want_full!="n":
      if want_full=="y":
        i=1
        for key,value in review_long_movies.items():
          print(str(i)+". "+key)
          #print(list(review_long_movies)[i-1])
          i+=1
        which_wrong_input=True
        while which_wrong_input:          
          which=input("Which full review do you want? ")
          if which.isdigit():
            which_wrong_input=False
            if int(which)>len(list(review_long_movies)) or int(which)<1:
              which_wrong_input=True
              print("Please select a movie in list")
          else:
            print("That's not a number!")
            which_wrong_input=True
        print(list(review_long_movies.values())[int(which)-1])
      elif want_full!="n":
        print("Please give proper response")
      want_full=input("Do you want to see full review of another movie? y/n ")
  another_movie=input("Do you want to search another movie? y/n ")
  while another_movie!="y":    
    if another_movie=="n":
      sys.exit("Thanks for using Emre Özincegedik's product. Good bye!")
    elif another_movie!="y":
      print("Please give proper response!")
    another_movie=input("Do you want to search another movie? y/n ")
