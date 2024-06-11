#1. Write a  Python program to sum all the items in a list.
def sum_list(num_list):
    num_sum = 0
    for num in num_list:
        if None in num_list:
            return "ERROR"
        else:
            num_sum += num

    return num_sum

num_list1 = [78,6,1,2,3,4,-8]


print(sum_list(num_list1))

#2. Write a  Python program to multiply all the items in a list.
def multiply_list(num_list):
    num_sum = 1
    for num in num_list:
        if None in num_list:
            return "ERROR"
        else:
            num_sum *= num

    return num_sum

print(multiply_list(num_list1))


#3. Write a Python program to get the largest number from a list.
def largest_from_list(num_list):
    max_num = num_list[0]
    if None in num_list:
        return "ERROR"
    else:
        for num in num_list[1:]:
            if num > max_num:
                max_num = num
        return max_num


print(largest_from_list(num_list1))

#4. Write a Python program to get the smallest number from a list.
def smallest_from_list(num_list):
    small_num = num_list[0]
    if None in num_list:
        return "ERROR"
    else:
        for num in num_list[1:]:
            if num < small_num:
                small_num = num
        return small_num

print(num_list1[:-1])
print(smallest_from_list(num_list1))

list_test = [10,20,30,40,50,60,70,80]

print(list_test[1:-3])

##5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
def count_string(string_list):
    count = 0
    string_list_count = []
    for word in string_list:
        if len(word) >= 2 and word[0] == word[-1]:
            string_list_count.append(word)
    return len(string_list_count)


string_list1 = ['abc', 'xyz', 'aba', '1221',"taz","kayak"]
print(count_string(string_list1))


##7. Write a  Python program to remove duplicates from a list.

def remove_duplicate(dup_list):
    non_dup_list = []
    for object in dup_list:
        if object not in non_dup_list:
            non_dup_list.append(object)
    return non_dup_list

duplicate_list = ['Red','Red','Green', 'Green', 'White', 'Black', 'Pink', 'Yellow']

print(remove_duplicate(duplicate_list))


##11. Write a Python function that takes two lists and returns True if they have at least one common member.

def find_common_member(list1,list2):
    for word in list1:
        if word in list2:
            # print(word)
            return True
        
color_list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color_list2 = ['purple', 'Blue',"Red"]

print(find_common_member(color_list1,color_list2))


print(duplicate_list.count('Red'))

##6. Write a Python function to check if a list is a palindrome or not. Return true otherwise false.

def check_palindrome(pal_list):
    empty_list = []
    for rev_char in reversed(pal_list):
        empty_list.append(rev_char)
    if empty_list == pal_list:
        return True
    else:
        return False

pal_list1 = ['Red', 'Blue',"Green","Red"]
print(check_palindrome(pal_list1))

##8. Write a Python function to remove duplicates from a list while preserving the order.

def remove_duplicates(dup_list):
    new_list = []
    for obj in dup_list:
        if obj not in new_list:
            new_list.append(obj)
    return new_list


dup_list2 = ['purple', 'Blue',"Red","Red"]
non_dup_list = ['purple', 'Blue',"Red"]

print(remove_duplicates(dup_list2))

dup_list2.sort()
print(dup_list2)