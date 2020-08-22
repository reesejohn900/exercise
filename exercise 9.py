import requests
import json

url = 'http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=fda04b42398b4188a29d80d57afdbe67'

r = requests.get(url)
r = r.text



a = json.loads(r)
b = a['articles']
print(a)
f = open('parth.txt','w+')
c = len(b)

for items in b:
     for values in items:
         c = 'title'
     f.write('the next news is')
     f.write(items[c])




f.close()

def speak(str):
    import win32com.client
    speak = win32com.client.Dispatch("SAPI.SpVoice")
    speak.Speak(str)

f_1 = open('parth.txt','r')
f_1 = f_1.readlines()
f_1 = str(f_1)


speak(f_1)






