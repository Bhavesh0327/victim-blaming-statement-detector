from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import sent_tokenize, word_tokenize 

statement="what was she wearing"

conn=[]
print(len(conn))
list1=word_tokenize(statement)
f2 = open("index2.txt" , "r")

with open('index2.txt') as f:
	roughlist = [line.rstrip('\n') for line in f]

for i in roughlist:
	list2=word_tokenize(i)
	if len(list2) == 2:
		try:
			y1=(sentence_bleu([list2], list1, weights=(1, 0)))
			y2=(sentence_bleu([list2], list1, weights=(0, 1)))
			if y1>0.1:	
				print(y1)
				conn.append(y1)
			if y2>0.1:
				print(y2)
				conn.append(y2)
		except:
			pass
	elif len(list2) == 3:
		try:
			y1=(sentence_bleu([list2], list1, weights=(1, 0,0)))
			y2=(sentence_bleu([list2], list1, weights=(0, 1,0)))
			y3=(sentence_bleu([list2], list1, weights=(0,0, 1)))
			if y1>0.1:
				print(y1)
				conn.append(y1)
			if y2>0.1:
				print(y2)
				conn.append(y2)
			if y3>0.1:
				print(y3)
				conn.append(y3)
		except:
			pass
	elif len(list2) == 4:
		y1=(sentence_bleu([list2], list1, weights=(1, 0,0,0)))
		y2=(sentence_bleu([list2], list1, weights=(0, 1,0,0)))
		y3=(sentence_bleu([list2], list1, weights=(0,0, 1,0)))
		y4=(sentence_bleu([list2], list1, weights=(0,0,0, 1)))
		if y1>0.1:
			print(y1)
			conn.append(y1)
		if y2>0.1:
			print(y2)
			conn.append(y2)
		if y3>0.1:
			print(y3)
			conn.append(y3)
		if y4>0.1:
			print(y4)
			conn.append(y4)	
			
if len(conn)>0:
	print("yes")	
	
