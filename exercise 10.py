import requests
import pickle

r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

r = r.text
r.split(' ')
f = open('parth.txt','w+')
f.write(r)

f.close()

f_1 = open('parth.txt','r+')
q = f_1.readlines()


list = []

for items in q:
    items = items.strip('\n')
    list.append(items)



f_1.close()


file = 'pickle module.txt'
file_1 = open(file,'wb')
pickle.dump(list,file_1)
file_1.close()

file_2 = open('pickle module.txt','rb')
my_pickle = pickle.load(file_2)
print(my_pickle)

file_2.close()