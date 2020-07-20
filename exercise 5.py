def getdate():
    import datetime
    return datetime.datetime.now()
def log():
    if a==1:
        if b==1:
            hf= open('harry_food.txt','a')
            q=input()
            hf.write(q)
            hf.close()
        elif b==2:
            he=open('harry_exercise.txt','a')
            w=input()
            he.write(w)
            he.close()
        else:
            print('wrong choice')
    elif a==2:
        if b==1:
            rf=open('rohan_food.txt','a')
            e=input()
            rf.write(q)
            rf.close()
        elif b==2:
            re=open('rohan_exercise.txt','a')
            r=input()
            re.write(w)
            re.close()
        else:
            print('wrong choice')
    elif a==3:
        if b==1:
            hmf =open('hammad_food.txt','a')
            t=input()
            hmf.write(q)
            hmf.close()
        elif b==2:
            hme=open('hammad_exercise.txt','a')
            w=input()
            hme.write(w)
            hme.close()
        else:
            print('wrong choice')

def retrive():
    if a == 1:
        if b == 1:
            hf= open('harry_food.txt')
            hf.read()
            hf.close()
        elif b == 2:
            he=open('harry_exercise.txt')
            he.read()
            he.close()
        else:
            print('wrong choice')
    elif a == 2:
        if b == 1:
            rf=open('rohan_food.txt')
            rf.read()
            rf.close()
        elif b == 2:
            re=open('rohan_exercise.txt')
            re.read()
            re.close()
        else:
            print('wrong choice')
    elif a == 3:
        if b == 1:
            hmf=open('hammad_food.txt')
            hmf.read()
            hmf.close()
        elif b == 2:
            hme=open('hammad_exercise.txt')
            hme.read()
            hme.close()
        else:
            print('wrong choice')

a=int(input('enter your choice\n'
                '1 for harry\n'
                '2 for rohan\n'
                '3 for hammad\n'))
b=int(input('press\n'
            '1 for food\n'
            '2 for exercise\n'))
c=int(input('1 for log \n'
            '2 for retrive\n'))
if c==1:
    log()
elif c==2:
    retrive()
else:
    print(' wrong choice ')
