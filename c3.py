import time

max_car = 5
cur_car = 0
car_lst = []


class car():
    def __init__(self, platenumber, owner, contantway, balance=20, time1=0, time2=0):
        self.platenumber = platenumber
        self.owner = owner
        self.contantway = contantway
        self.balance = balance
        self.time1 = time1
        self.time2 = time2

    def park(self):
        if len(car_lst) < max_car:
            self.time1 = time.time()
            car_lst.append(self)
            print('停车成功.')
        else:
            print('车库已满.')

    def exit(self):
        a = len(car_lst) - 1 if len(car_lst) == max_car else  len(car_lst)
        for i in range(0, a):
            if car_lst[i].platenumber == self.platenumber:
                carex = car_lst[i]
                car_lst.remove(car_lst[i])
                carex.time2 = time.time()
                tt = float((carex.time2 - carex.time1) / 3600)
                print('停车时间%f小时,停车费用%f元.' % (tt, float(tt / 5)))
            else:
                if i == len(car_lst) - 1:
                    print('该汽车从未进入， 请联系管理员.')


while True:
    cho = input(
        '''
        请选择功能：
        1.停车
        2.出车
        3.退出系统   
        '''
    )
    if cho == '3':
        break
    elif cho == '1':
        if len(car_lst) >= max_car:
            print('车库已满.')
        else:
            pla = input('输入车牌号：')
            own = input('输入车主名：')
            cw = input('输入联系方式：')
            c = car(pla, own, cw)
            c.park()
    elif cho == '2':
        if len(car_lst) == 0:
            print('车库为空， 请联系管理员.')
        else:
            pl = input('输入车牌号：')
            carr = car(pl, 0, 0)
            carr.exit()
    else:
        print('输入错误，请重新选择.')
    time.sleep(2)
    continue