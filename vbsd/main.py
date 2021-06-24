from strsimpy.jaro_winkler import JaroWinkler
from nltk.tokenize import sent_tokenize, word_tokenize 
import csv 
import pandas as pd
from nltk.translate.bleu_score import sentence_bleu






filename = "Andbrain_DataSet.csv"
jarowinkler = JaroWinkler()
#111111111111111111111111111111111111111111111111111
statement= str(input())
f= open("dataset.txt", "r")

with open('dataset.txt') as f:
    mylist= [line.rstrip('\n') for line in f]
for line in mylist:
    sim_index=jarowinkler.similarity(line, statement)
    if sim_index>0.80:
        print("1:-  "+str(sim_index))
        print("yes, it is similar to a victim blaming statement")
        if sim_index != 1 and sim_index>0.8:
            break
f.close()
#222222222222222222222222222222222222222222222222222
initial_score=0
list1 = word_tokenize(statement)
for i in list1:
	y=0
	x=i+ " "
	df = pd.read_csv(filename, usecols = ['word' , 'disgust' , 'anger' , 'sad'])
	for i in enumerate(df.word):
	    if x == i[1]:
	        y=(df.disgust)[i[0]]*0.45+(df.anger)[i[0]]*0.35+(df.sad)[i[0]]*0.2
	initial_score=initial_score+y
	
print("Blaming tone score:-  "+str(initial_score*100))

#333333333333333333333333333333333333333333333333333

f1 = open("index1.txt" , "r")

with open('index1.txt') as f:
	swear= [line.rstrip('\n') for line in f]

for word in list1:
	if word in swear:
		print("It is a very offensive statement")

f1.close()
#4444444444444444444444444444444444444444444444444444

conn=[]
list1=word_tokenize(statement)
f2 = open("index2.txt" , "r")

with open('index2.txt') as f:
	roughlist = [line.rstrip('\n') for line in f]

for i in roughlist:
	list2=word_tokenize(i)
	if len(list2) == 2:
		y1=(sentence_bleu([list2], list1, weights=(1, 0)))
		y2=(sentence_bleu([list2], list1, weights=(0, 1)))
		if y1>0.1:
			conn.append(y1)
		if y2>0.1:
			conn.append(y2)
	elif len(list2) == 3:
		y1=(sentence_bleu([list2], list1, weights=(1, 0,0)))
		y2=(sentence_bleu([list2], list1, weights=(0, 1,0)))
		y3=(sentence_bleu([list2], list1, weights=(0,0, 1)))
		if y1>0.1:
			conn.append(y1)
		if y2>0.1:
			conn.append(y2)
		if y3>0.1:
			conn.append(y3)
	elif len(list2) == 4:
		y1=(sentence_bleu([list2], list1, weights=(1, 0,0,0)))
		y2=(sentence_bleu([list2], list1, weights=(0, 1,0,0)))
		y3=(sentence_bleu([list2], list1, weights=(0,0, 1,0)))
		y4=(sentence_bleu([list2], list1, weights=(0,0,0, 1)))
		if y1>0.1:
			conn.append(y1)
		if y2>0.1:
			conn.append(y2)
		if y3>0.1:
			conn.append(y3)
		if y4>0.1:
			conn.append(y4)	
			
if len(conn)>0:
	print("Yes, it is a victim blaming statement.")	
