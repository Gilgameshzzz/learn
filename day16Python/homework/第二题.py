"""__author__ = 余婷"""
"""
1.建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，速度等成员变量，
并通过不同的构造方法创建实例。至少要求 汽车能够加速 减速 停车。 
再定义一个小汽车类CarAuto 继承Auto 并添加空调、CD等成员变量 覆盖加速 减速的方法
"""


class Auto:
    def __init__(self,tyre_count=4, color='', weight=0, speed=0):
        self.tyre_count = tyre_count
        self.color = color
        self.weight = weight
        self.speed = speed

    def add_speed(self):
        """加速"""
        new_speed = self.speed + 10
        # 加速最大能增加到200
        if new_speed >= 200:
            new_speed = 200
        self.speed = new_speed

    def sub_speed(self):
        """减速"""
        new_speed = self.speed - 10
        # 减速最少减到0
        if new_speed < 0:
            new_speed = 0
        self.speed = new_speed

    def stop(self):
        """停车"""
        self.speed = 0


class CarAuto(Auto):
    def __init__(self,tyre_count=4, color='', weight=0, speed=0):
        super.__init__(tyre_count, color, weight, speed)
        self.air_conditioning = None
        self.CD = None

    def add_speed(self):
        """加速"""
        new_speed = self.speed + 20
        # 加速最大能增加到200
        if new_speed >= 250:
            new_speed = 250
        self.speed = new_speed

    def sub_speed(self):
        """减速"""
        new_speed = self.speed - 20
        # 减速最少减到0
        if new_speed < 0:
            new_speed = 0
        self.speed = new_speed



if __name__ == '__main__':
    pass