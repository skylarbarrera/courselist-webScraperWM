import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver



Subjects = [];
# Term = 202020
# Subject = CSCI
#classInfo = 'https://courselist.wm.edu/courselist/courseinfo/addInfo?fterm=202020&fcrn=23740'

class SingleSubjectScraper:
    def __init__(self,term,subject):
        self.term = term
        self.subject = subject
        self.url = 'https://courselist.wm.edu/courselist/courseinfo/searchresults?term_code={}&term_subj={}&attr=0&attr2=0&levl=0&status=0&ptrm=0&search=Search'.format(self.term,self.subject)


        self.driver = self.__setupDriver();
        self.classes = self.__pullClasses();


    def __setupDriver(self):

        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        chrome_driver_binary = "/usr/local/bin/chromedriver"
        return webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    def __pullClasses(self):
        self.driver.get(self.url)
        sleep(3)

        soup = BeautifulSoup(self.driver.page_source,'html.parser')
        #print(soup)


        allClasses = soup.find_all("tr")


        allClassesData = []
        for i in allClasses:
            oneClass = i.find_all("td");
            tempClass =[]
            for item in oneClass:
                tempClass.append(item.text.strip())

            allClassesData.append(tempClass)
        allClassesData.pop(0)
        self.driver.quit()
        return allClassesData


    def getClasses(self):
        return self.classes;
