user_number = int(input("Please Provide a Number: "))

for number in range(1,user_number+1):
    if user_number % number == 0:
        print(number)

# print(10%2)