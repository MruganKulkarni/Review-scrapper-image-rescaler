import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd

link=input('Paste the link of the Reviews page here:\n')
reviewlink = link + "&page=" + str(1)
page=reviewlink[+1:]
page=int(page)
for i in range(page+1,100):
    l=reviewlink.rstrip('2')
    i=str(i)
    final=l+i
    print(final)
    page=requests.get(final)
    page.content
    print("******************************************************************************************************************")
    print("******************************************************************************************************************")
    soup=BeautifulSoup(page.content,'html.parser')
    #print(soup.prettify())
    print("******************************************************************************************************************")
    print("******************************************************************************************************************")
    review2=[]
    for j in soup.find_all('div',class_="_6t1WkM _3HqJxg"):
        review2.append(j.text.split("."))
    
    data1={"reviews":review2[0]}
    
    #data=pd.DataFrame(data=data1)
    #data.to_csv('output.csv')

   # df = pd.DataFrame(data1)
    #df.to_csv('output22.csv', index=False)  


print(data)
print("******************************************************************************************************************")
print("********************************************************************")