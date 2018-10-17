import time 
from car import Car
from parkingRecord import Record
class CarOwner():
    def __init__(self,owner_id,owner_name,owner_phone):
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.owner_phone = owner_phone
    
    def get_info_owner(self):
        print('获取车主信息：')
        print('车主id：<%s> 车主：<%s> 电话:<%s>  '
              % (self.owner_id, self.owner_name,self.owner_phone))

    def enter_parking(self):
        print('进入停车场')
        Record.time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(Record.time1)

    def enter_space(self):
        print('驶入车位')
        Record.time2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(Record.time2)

    def leave_space(self):
        print('驶出车位')
        Record.time3 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(Record.time3)
    
    def leave_parking(self):
        print('驶出停车场')
        Record.time4 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(Record.time4)

    