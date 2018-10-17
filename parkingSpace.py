class ParkingSpace():
    
    def __init__(self,parking_space_name,price):
        self.parking_space_name = parking_space_name
        self.price =  price

    def get_info_space(self):
        print('获取车位信息：')
        print('车位名称：<%s> 价格：<%s>'
              % (self.parking_space_name, self.price))