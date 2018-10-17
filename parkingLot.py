class ParkingLot():

    def __init__(self,parking_lot_name,max_parking,used_parking):
        self.parking_lot_name = parking_lot_name
        self.max_parking = max_parking
        self.used_parking = used_parking

    def Calculation(self):
        print('<判断停车场使用情况>')
        number = int(self.max_parking) - int(self.used_parking)
        if number > 0:
            print('剩余车位数量为：'+str(number)+' ;请入场停车')
        else:
            print('车位不足无法停车')
