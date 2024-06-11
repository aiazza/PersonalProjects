# user_string = input("Please provide a string: ")
user_string = "kayako"

user_string_list = []
user_string_list_back = []

for letter in user_string:
    user_string_list.append(letter)
    
user_string_list_back.extend(user_string_list[::-1])

user_string_list_string = ''.join(user_string_list)
user_string_list_string_back = ''.join(user_string_list_back)


if user_string_list == user_string_list_back:
    print("This string is a Palindrome" , user_string_list_string, " is the same as ", user_string_list_string_back)

if user_string_list == user_string_list_back:
    print("This string is a Palindrome ")
else:
    print("NOT PALINDROME")