class Order():
    def __init__(self,order_no,order_money,pay_way,pay_status,order_status):
        self.order_no = order_no
        self.order_money = order_money
        self.pay_way = pay_way
        self.pay_status = pay_status
        self.order_status = order_status

    def get_info_order(self):
        print('获取订单信息：')
        print('订单编号：<%s> 订单金额：<%s> 支付方式:<%s> 支付状态:<%s> 订单状态：<%s> '
              % (self.order_no, self.order_money,self.pay_way,self.pay_status, self.order_status))