import random
import time
from datetime import datetime


class parking_lot:
    def __init__(self, floors, floor_capacity, fee_per_hour):
        self.floors = floors
        self.floor_capacity = floor_capacity
        self.cars = []
        self.fee_per_hour = fee_per_hour
        self.parking_space_number = dict(list(enumerate(self.cars)))
        self.max_capacity = self.floors * self.floor_capacity
       
    def get_car_in_parking_space_number(self,brand):
        Brand_for_ticket_id = ""
        dict_items = self.parking_space_number.items()
        for key, value in dict_items:
            if value == brand:
                Brand_for_ticket_id = key
                return key

    def add_car_checkin(self, brand):
        self.brand = brand
        if self.max_capacity == len(self.cars):
            print("Parking Full - Please come again later")
        else:
            self.cars.append(brand)
            self.ticket_table = dict(list(enumerate(self.cars, 1)))
            print("Welcome to the parking lot, your unique ticket is : #", self.get_brand_per_ticket_id(brand), "\n Your car is a : ", brand)
            


    def calculate_ticket_fee_checkout(self, brand, car_type, time_spent):
        self.time_spent = time_spent
        self.brand = brand
        self.ticket_id = self.get_brand_per_ticket_id(brand)
        self.brand = brand
        self.car_type = car_type
        if brand not in self.cars:
            print("Sorry, Your car is not checked in.")
            pass
        elif self.car_type == "SUV":
            fee = self.fee_per_hour * 2 * self.time_spent
            print("Your ticket ID is : #", self.get_brand_per_ticket_id(brand), "This is your SUV Fee : $", fee, "\n Your car is a : ", brand)
        elif self.car_type == "Sedan":
            fee = self.fee_per_hour * self.time_spent
            print("Your ticket ID is : #", self.get_brand_per_ticket_id(brand), "This is your Sedan Fee : $", fee, "\n Your car is a : ", brand)

class ticket(parking_lot):
    def __init__(self):
        pass
    def check_in_timestamp(self):
        currenttime = datetime.now().strftime('%H:%M')
        return currenttime
    def check_out_timestamp_diff(self):
        currenttime = datetime.now().strftime('%H:%M')
        ticket.check_in_timestamp
        return currenttime

class car(parking_lot):
    def __init__(self, brand, car_type):
        self.brand = brand
        self.car_type = car_type
        self.enter_parking_lot()
    def enter_parking_lot(self):
        parking_space_number = parking_lot.get_car_in_parking_space_number(self.brand)
        if parking_space_number is not False:
            return parking_space_number



C1 = car("Honda", "SUV")
C2 = car("Toyota", "Sedan")
C3 = car("Mazda","Sedan")
C4 = car("Bugatti", "SUV")

print(C1.car_checkin())

parkinglot = parking_lot(1,3,13)

parkinglot.add_car_checkin(C1.brand)

# Result : Welcome to the parking lot, your unique ticket is : # 1 
# Your car is a :  Honda

parkinglot.add_car_checkin(C2.brand)

# Welcome to the parking lot, your unique ticket is : # 2 
#  Your car is a :  Toyota

parkinglot.add_car_checkin(C3.brand)

# Welcome to the parking lot, your unique ticket is : # 3 
#  Your car is a :  Mazda

parkinglot.add_car_checkin(C4.brand)

# Parking Full - Please come again later

parkinglot.calculate_ticket_fee_checkout(C1.brand, C1.car_type, 130)

# Your ticket ID is : # 1 This is your SUV Fee : $ 3380
#  Your car is a : Honda

parkinglot.calculate_ticket_fee_checkout(C2.brand, C2.car_type, 24)

# Your ticket ID is : # 2 This is your Sedan Fee : $ 312 
#  Your car is a :  Toyota

parkinglot.calculate_ticket_fee_checkout(C3.brand, C3.car_type, 2400)

# Your ticket ID is : # 3 This is your Sedan Fee : $ 31200 
#  Your car is a :  Mazda

parkinglot.calculate_ticket_fee_checkout(C4.brand, C4.car_type, 2)

# Sorry, Your car is not checked in.

t1 = ticket()

print(t1.check_in_timestamp())
print(t1.check_out_timestamp_diff())