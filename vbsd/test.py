with open('dataset.txt') as f:
    mylist = [line.rstrip('\n') for line in f]

line="yeah hey there"

mylist.append(line)
print(mylist)
