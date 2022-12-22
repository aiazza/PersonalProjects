import random


class car:
    def __init__(self, brand, car_type):
        self.brand = brand
        self.car_type = car_type
        # self.time_spent = time_spent
        

class parking_lot:
    def __init__(self, floors, floor_capacity,fee_per_hour):
        self.floors = floors
        self.floor_capacity = floor_capacity
        self.cars = []
        self.fee_per_hour = fee_per_hour
        self.ticket_table = dict(list(enumerate(self.cars)))

    def get_brand_per_ticket_id(self,brand):
        Brand_for_ticket_id = ""
        dict_items = self.ticket_table.items()
        for key, value in dict_items:
            if value == brand:
                Brand_for_ticket_id = key
                return key

    def add_car_checkin(self, brand):
        self.brand = brand
        max_capacity = self.floors * self.floor_capacity
        if max_capacity == len(self.cars):
            print("Parking Full - Please come again later")
        else:
            unique_ticket = random.randint(0, 5)
            ticket_table = {unique_ticket: brand}
            self.cars.append(brand)
            self.ticket_table = dict(list(enumerate(self.cars, 1)))
            print("Welcome to the parking lot, your unique ticket is : #", self.get_brand_per_ticket_id(brand),"\n Your car is a : ", brand)
            


    def calculate_ticket_fee_checkout(self,brand,car_type, time_spent):
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
            print("Your ticket ID is : #",self.get_brand_per_ticket_id(brand), "This is your SUV Fee : $", fee, "\n Your car is a : ", brand)
        elif self.car_type == "Sedan":
            fee = self.fee_per_hour * self.time_spent
            print("Your ticket ID is : #",self.get_brand_per_ticket_id(brand), "This is your Sedan Fee : $",fee,"\n Your car is a : ", brand)




C1 = car("Honda", "SUV")
C2 = car("Toyota", "Sedan")
C3 = car("Mazda","Sedan")
C4 = car("Bugatti", "SUV")

parkinglot = parking_lot(1,3,13)

parkinglot.add_car_checkin(C1.brand)
parkinglot.add_car_checkin(C2.brand)
parkinglot.add_car_checkin(C3.brand)
parkinglot.add_car_checkin(C4.brand)



parkinglot.calculate_ticket_fee_checkout(C1.brand,C1.car_type, 130)
parkinglot.calculate_ticket_fee_checkout(C2.brand,C2.car_type, 24)
parkinglot.calculate_ticket_fee_checkout(C3.brand,C3.car_type, 2400)
parkinglot.calculate_ticket_fee_checkout(C4.brand,C4.car_type, 2)



