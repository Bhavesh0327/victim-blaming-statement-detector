from nltk.translate.bleu_score import sentence_bleu
reference = [['this' ,'is' ,'totally' ,'against' ,'indian' ,'culture']]
candidate = ['this' ,'is' ,'totally' ,'against' ,'indian' ,'culture']
print('Individual 1-gram: %f' % sentence_bleu(reference, candidate, weights=(1, 0)))
print('Individual 2-gram: %f' % sentence_bleu(reference, candidate, weights=(0, 1)))
#print('Individual 3-gram: %f' % sentence_bleu(reference, candidate, weights=(0, 0, 1)))
