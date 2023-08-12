# Source https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html 

# For this exercise, we will keep track of when our friend’s birthdays are, 
# and be able to find that information based on their name. 
# Create a dictionary (in your file) of names and birthdays. 
 #When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. 
# The interaction should look something like this:

#>>> Welcome to the birthday dictionary. We know the birthdays of:
#Albert Einstein
#Benjamin Franklin
#Ada Lovelace
#>>> Who's birthday do you want to look up?
#Benjamin Franklin
#>>> Benjamin Franklin's birthday is 01/17/1706.

Birthday_dict = {'Naruto Uzumaki':'10/10/1999','Monkey D. Luffy': '05/10/1997' }
print(f"Welcome to the birthday dictionary. We know the birthdays of :\n{[key for key, value in Birthday_dict.items()]} ")
user_input = input("Who's birthday do you want to look up?\n")
while user_input not in Birthday_dict:
    user_input = input("Who's birthday do you want to look up?\n")
print(f"{user_input}'s birthday is {Birthday_dict[user_input]}")