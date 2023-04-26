import requests, webbrowser
from bs4 import BeautifulSoup
ans = "AIDS"
print ("gooogling.....")
google_search = requests.get ("https://www.google.com/search?q="+ ans)
soup = BeautifulSoup(google_search.text, 'html.parser')
print(soup.prettify())
search_res=soup.select('.rQMQod')
print(search_res)
# search_res=soup.find(class_='.Ap5OSd').find(class_='BNeawe s3v9rd AP7Wnd')


lensearch=len(search_res)
# print(lensearch)
i=0
while(i<lensearch):
    print(search_res[i].string)
    i+=1;
    break;
# soup.select(".r")
