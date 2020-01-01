from SingleSubjectScraper import SingleSubjectScraper
from subjectScraper import SubjectScraper
import pandas as pd
import numpy as np


test = SubjectScraper()

subjects = test.getSubjects()


#new = SingleSubjectScraper("202020", 'CSCI')
df = pd.DataFrame( columns = ["CRN","COURSE ID", "ATTRIBUTES", "NAME", "PROFESSOR","CREDITS","DATE/TIME","CAPACITY","CURRENT","AVAILABLE","STATUS"])
#
#new = SingleSubjectScraper("202020", subject[0])

#    newDf = pd.DataFrame( new.getClasses(), columns = ["CRN","COURSE ID", "ATTRIBUTES", "NAME", "PROFESSOR","CREDITS","DATE/TIME","CAPACITY","CURRENT","AVAILABLE","STATUS"])
for subject in subjects:

   new = SingleSubjectScraper("202020", subject[0])
   newDf = pd.DataFrame( new.getClasses(), columns = ["CRN","COURSE ID", "ATTRIBUTES", "NAME", "PROFESSOR","CREDITS","DATE/TIME","CAPACITY","CURRENT","AVAILABLE","STATUS"])
   df = df.append(newDf)

#df.transpose()
print(df)

export_csv = df.to_csv("allClasses.csv")
