from datetime import datetime


class parking_lot():
    def __init__(self, floors, floor_capacity):
        self.floors = floors
        self.floor_capacity = floor_capacity
        self.cars = []
        self.occupied_parking_spaces = []
        self.max_capacity = self.floors * self.floor_capacity

    def get_parking_space_number(self, parking_space):
        self.parking_space_number = dict(list(enumerate(self.occupied_parking_spaces, 1)))
        dict_items = self.parking_space_number.items()
        for key, value in dict_items:
            if value == parking_space:
                self.parking_space_number = key
                return key

    def calculate_available_space(self):
        self.occupied_space = len(self.occupied_parking_spaces)
        self.available_spaces = self.max_capacity - len(self.occupied_parking_spaces)
        print("There are currently {} cars parked in the parking lot\nThere are {} spaces available in the parking lot".format(self.occupied_space, self.available_spaces))

    def add_car_checkin(self,car):
        self.unique_ticket = ticket()
        car.ticket = self.unique_ticket
        self.unique_parking_space = parking_space(car)
        if self.calculate_available_space == self.max_capacity:
            print("Parking Full - Please come again later")
        else:
            self.occupied_parking_spaces.append(self.unique_parking_space)
            car.ticket = self.unique_ticket
            self.unique_parking_space.parking_space = car.parking_space
            self.unique_parking_space.parking_space_number = self.get_parking_space_number(self.unique_parking_space)
            car.parking_space = self.unique_parking_space
            self.unique_ticket.checkin_timestamp = self.unique_ticket.check_in_timestamp()
            print("Welcome to the parking lot, your unique ticket is : #", car.parking_space.parking_space_number, "\nYour car is a : ", car.brand,"\nYou parked at : ", self.unique_ticket.checkin_timestamp,"\n========================")

    def car_checkout(self,car):
        print("=========\nCHECKOUT\n=======")
        # self.unique_ticket.checkout_timestamp = self.add_car_checkin.__getattribute__        
        car_ticket = car.ticket
        car_ticket.checkout_timestamp = car_ticket.check_out_timestamp()
        # print("timestamp",car.ticket.checkout_timestamp)
        if car.parking_space not in self.occupied_parking_spaces:
            print("Your car is not registered in this parking")
        else:
            print("You have checked in at", car.ticket.checkin_timestamp, "You are checking out at", car.ticket.checkout_timestamp)





class parking_space():
    def __init__(self, car):
        self.car = car
        self.parking_space_number = ""


class automobile():
    def __init__(self, brand, car_type, parking_lot):
        self.brand = brand
        self.car_type = car_type
        self.parking_lot = parking_lot
        self.parking_space = ""
        self.ticket = ""

    def check_for_ticket_id(self):
        if not self.parking_space:
            return False
        else:
            return True


class ticket(parking_lot):
    def __init__(self):
        self.check_in_timestamp()
        self.ticket_id = ""
        self.checkin_timestamp = ""
        self.checkout_timestamp = ""
    def check_in_timestamp(self):
        currenttime = datetime.now().strftime('%H:%M')
        return currenttime
    def check_out_timestamp(self):
        currenttime = datetime.now().strftime('%H:%M')
        return currenttime
        
parking_lot1 = parking_lot(1,5)

C1 = automobile("Honda", "SUV", parking_lot1 )
C2 = automobile("Toyota", "Sedan", parking_lot1)

# C1.check_for_ticket_id()

# parking_lot1.add_car_checkin(C1)
# parking_lot1.add_car_checkin(C2)

# parking_lot1.calculate_available_space()

# parking_lot1.get_parking_space_number(C1)

parking_lot1.car_checkout(C1)

# print(parking_lot1.occupied_parking_spaces)

# parking_lot2 = parking_lot(1,5)

# parking_lot2.car_checkout(C1)

# print("ticket", C1.ticket.checkin_timestamp)
