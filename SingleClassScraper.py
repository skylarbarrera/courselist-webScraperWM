import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver

url = 'https://courselist.wm.edu/courselist/courseinfo/searchresults?term_code=202020&term_subj=CSCI&attr=0&attr2=0&levl=0&status=0&ptrm=0&search=Search'
classInfo = 'https://courselist.wm.edu/courselist/courseinfo/addInfo?fterm=202020&fcrn=23740'

Subjects = [];


options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/usr/local/bin/chromedriver"
response = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
response.get(url)
sleep(3)



#Macintosh HD⁩ ▸ ⁨Applications⁩ ▸ ⁨Google Chrome Canary⁩ ▸ ⁨Contents⁩ ▸ ⁨MacOS⁩
#print(response.page_source)
#page = requests.get(url)
soup = BeautifulSoup(response.page_source,'html.parser')
#print(soup)


allClasses = soup.find_all("tr")


allClassesData = []
for i in allClasses:
    oneClass = i.find_all("td");
    tempClass =[]
    for item in oneClass:
        tempClass.append(item.text.strip())

    allClassesData.append(tempClass)

    #print(toneClass));
