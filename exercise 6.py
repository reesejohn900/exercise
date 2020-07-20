import random
b =0
p =0
for i in range (1,11):
    list=['stone','paper','scissor']
    a=random.choice(list)
    n=int(input('enter your choice\n1 stone\n2 paper\n3 scissor\n'))
    if a==list[0] and n==1:
        print('tie')
    elif a==list[0] and n==2:
        print('you won')
        p = p+1
    elif a==list[0] and n==3:
        print('computer won')
        b = b+1
    elif a==list[1] and n==1:
        print('computer won')
        b =b+1
    elif a==list[1] and n==2:
        print('tie')
    elif a==list[1] and n==3:
        print('you won')
        p = p+1
    elif a==list[2] and n==1:
        print('you won')
        p = p+1
    elif a==list[2] and n==2:
        print('computer won')
        b = b+1
    elif a==list[2] and n==3:
        print('tie')
    else:
        print('invalid choice')
print('you won :',p)
print('computer',b)

