# importing csv module 
import csv 
import pandas as pd
# csv file name 
filename = "Andbrain_DataSet.csv"
y=0
x=input()+ " "
df = pd.read_csv(filename, usecols = ['word' , 'disgust' , 'anger' , 'sad'])
for i in enumerate(df.word):
    if x == i[1]:
        y=(df.disgust)[i[0]]*0.45+(df.anger)[i[0]]*0.35+(df.sad)[i[0]]*0.2
print(y)
