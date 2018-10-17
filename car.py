class Car():
    def __init__(self,car_num,car_owner,car_brand,car_color,car_model):
        self.car_num=car_num             # 车牌号
        self.car_owner=car_owner         # 车主
        self.car_brand=car_brand         # 品牌
        self.car_color=car_color         # 颜色
        self.car_model=car_model         # 型号

    def get_info(self):
        print('获取车辆信息：')
        print('车牌号：<%s> 车主：<%s> 品牌:<%s> 颜色:<%s> 型号：<%s> '
              % (self.car_num, self.car_owner,self.car_brand,self.car_color, self.car_model))
        