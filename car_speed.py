class car:
    def __init__(self,speed):
        print(f"If the speed of the car is {speed} the option for you is :")
        self.car_speed=speed
    def car_model1(self):
        if  self.car_speed>=500:
            print("Mclearn is the high speed car and best for you")
        else:
            print("Ferrari the best for you")
car=car(600)
car.car_model1()