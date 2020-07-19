from django.shortcuts import render
from bs4 import BeautifulSoup
import requests as r
# Create your views here.
def home(requests):
    site = r.get('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(site.content, 'html.parser')
    result = soup.find(class_="bg-blue")
    print(result.strong.text.strip())
    states = 36
    li = []
    for link in soup.find_all("tr"):
        if (states==0):
            break
        if states==36:
            pass
        else:
            li.append(link)
        states-=1
    table_data=[]
    for td in li: 
        t_row =[]
        x = td.find_all("td")
        for i in x:
            t_row.append(i.text)
        table_data.append(t_row)   
    return render(requests,'index.html',{'td':table_data})

