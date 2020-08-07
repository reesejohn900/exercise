import os

n = input('enter the working directory\n')
os.chdir(n)

a = input('enter the file name u want to protect\n')

for file in os.listdir(n):
    if file.endswith('.txt') and file != a:
        f = open(file,'r+')
        b = f.readline()
        c = b.title()
        f.seek(0)
        f.truncate()
        f.write(c)

        f.close()


d = input('enter the file extension u want to rename')

i=1

for file in os.listdir(n):
    if file.endswith(d):
        os.rename(file,str(i) + '.jpg')
        i = i+1
print('file renamed')