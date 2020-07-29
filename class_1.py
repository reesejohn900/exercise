class Time_1:
    def __init__(self,hour):
        self.hours = hour


class Time_2:
    def __init__(self,minute):
        self.minutes =minute


def addtime():
    a = t_1.hours + t_3.hours
    b = t_2.minutes + t_4.minutes

    if b > 60:
        a = a+1
        b = b-60
        print(str(a) + 'hours' + str(b) + 'minutes')

    else:
        print(str(t_1.hours+t_3.hours)+'hours'+str(t_2.minutes+t_4.minutes)+ 'minutes')

def display_time():
    c = t_1.hours + t_3.hours
    d = t_2.minutes + t_4.minutes
    print(str(a*60+b)+'minutes')


if __name__ == '__main__':
    t_1 = Time_1(2)
    t_3 = Time_1(3)
    t_2 = Time_2(52)
    t_4 = Time_2(30)

    print(str(t_1.hours) + 'hour' + str(t_2.minutes) + 'minutes')
    print(str(t_3.hours) + 'hour' + str(t_4.minutes) + 'minutes')

    a= t_1.hours+t_3.hours
    b= t_2.minutes+t_4.minutes


    addtime()
    display_time()
