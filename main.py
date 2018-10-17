import time
from car import Car
from carOwner import CarOwner
from parkingLot import ParkingLot
from parkingRecord import Record
from order import Order
from parkingSpace import ParkingSpace

def main():
    print('=====前方来车将进入停车场=====')
    
    parkingLot = ParkingLot('A区停车场',200,50)
    parkingLot.Calculation()
    
    car = Car('辽A567T5','liudi','大众','白色','轿车')
    car.get_info()
    
    carOwner = CarOwner(1,'liudi','13333333333')
    carOwner.get_info_owner()
    carOwner.enter_parking()
    carOwner.enter_space()
    carOwner.leave_space()

    parkingSpace = ParkingSpace('A区A001',5)
    parkingSpace.get_info_space()

    order = Order(10001,20,'现金','支付成功','订单完成')
    order.get_info_order()

    carOwner.leave_parking()



if __name__ == '__main__':
    main()