import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver

class SubjectScraper:
    def __init__(self):
        self.url = "https://courselist.wm.edu/courselist/"


        self.driver = self.__setupDriver();
        self.subjects = self.__pullSubjects();


    def __setupDriver(self):

        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        chrome_driver_binary = "/usr/local/bin/chromedriver"
        return webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    def __pullSubjects(self):
        self.driver.get(self.url)
        sleep(3)

        soup = BeautifulSoup(self.driver.page_source,'html.parser')
        option = soup.find(id = "term_subj")
        subjects = option.select('option[value]')

        allSubjects = [];
        for subject in subjects:
            allSubjects.append([
            subject.get('value'),
            subject.text
            ])



        allSubjects.pop(0)
        self.driver.quit()
        return allSubjects


    def getSubjects(self):
        return self.subjects;
