
class Vehicle1:
    def __init__(self, color, price, wheels):
        self.color = color
        self.price = price
        self.wheels = wheels
        self.speed = None

    def set_speed(self, speed=100):
        self.speed = speed

    def accelerate(self, amount):
        if self.speed is None:
            raise ValueError("Speed has not been set.")
        self.speed += amount
        return self.speed

    def decelerate(self, amount):
        if self.speed is None:
            raise ValueError("Speed has not been set.")
        self.speed -= amount
        return self.speed

    def print_info(self):
        print("Color:", self.color)
        print("Price:", self.price)
        print("Number of wheels:", self.wheels)
        print("Speed:", self.speed)

betty = Vehicle1('yellow', 2000.00, 4)
betty.set_speed()
betty.accelerate(10)
betty.print_info()
