
import json
# Source : https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
# This exercise is Part 2 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 3, and Part 4.

# In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.

# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

json_file_var = "birthday.json"

def load_json_file(json_file):
    with open(json_file, 'r') as f:
        Birthday_json = json.load(f)
    return Birthday_json

def update_birthday_json(json_dict, name, date):
    json_dict[name] = date
    with open(json_file_var, 'w') as f:
        json.dump(json_dict, f)
    print("Directory has been updated")


Birthday_json = load_json_file(json_file_var)

print(Birthday_json)


print(f"Welcome to the birthday dictionary. We know the birthdays of :\n{[key for key, value in Birthday_json.items()]} ")
user_choice = input("Do you want to update the directory or lookup a birthday ?\n1.update\n2.lookup\n")
if user_choice == "1":
    user_input_name = input("Please provide name of character\n")
    user_input_date = input("Please provide birthday date of character - format : MM/DD/YYYY\n")
    update_birthday_json(Birthday_json, user_input_name, user_input_date)
if user_choice == "2":
    user_input = input("Who's birthday do you want to look up?\n")
    while user_input not in Birthday_json:
        user_input = input("Who's birthday do you want to look up?\n")
    print(f"{user_input}'s birthday is {Birthday_json[user_input]}")
