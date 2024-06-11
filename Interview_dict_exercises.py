import csv
##1. Write a  Python script to sort (ascending and descending) a dictionary by value.
dictionary_sample = {0: 10, 1: 20, 5: 258, 3:5, 14: 10}
sorted_dict = sorted(dictionary_sample.items())
# print(sorted_dict)
converted_dict = dict(sorted_dict)
print(converted_dict)

##2. Write a Python script to add a key to a dictionary.
def add_key(dictionary, new_entries):
    dictionary.update(new_entries)
dictionary_sample2 = {0: 10, 1: 20, 5: 258, 3:5}
add_key(dictionary_sample2, {'color': 'RED',"size":"Medium"})
print(dictionary_sample2)

##3. Write a  Python script to concatenate the following dictionaries to create a new one.


def merge_dict(dict1, dict2, dict3):
    new_dict = {}
    dict_list = [dict1,dict2,dict3]
    for d in dict_list:
        new_dict.update(d)
    return new_dict
dic1={1:10, 2:20}
dic2={3:30, 4:40,"Color1": "Green"}
dic3={5:50,6:60,"Color2": "REEEED"}

print(merge_dict(dic1,dic2,dic3))



##4. Write a Python script to check whether a given key already exists in a dictionary.
def check_dict(dict1,key):
    for k in dict1.keys():
        if k == key:
            return True
        else:
            return False
dict_to_check = {'color': 'RED',"size":"Medium",'weight':0.75}
print(check_dict(dict_to_check,'color'))

##5. Write a Python program to iterate over dictionaries using for loops.
dict_for_loop = {'color': 'RED',"size":"Medium",'weight':0.75}

for d in dict_for_loop["color"]:
    print(d)

dict_for_loop.fromkeys
print(dict_for_loop)
# list = ["a","b","c","d","e","f","g"]
# for i in range(len(list[2:5])):
#     print(f"Element at index {i}: {list[i]}")


def return_csv(csvfile):
    with open(csvfile) as csv_file:
        csvlist = csv.reader(csv_file)
        for row in csvlist:
            print(row)
        print(csvlist)

print(return_csv("cities.csv"))

temp = []
empty_dict = {}
for key, value in dictionary_sample.items():
    print(value)
    if value not in temp:
        temp.append(value)
        empty_dict[key] = value
print(temp)
print(empty_dict)
dict_list = []
dictionary_items = dict_list.append(dictionary_sample.items())
print(dictionary_items)
# print(dictionary_items.count(10))

##5. Write a Python program to remove duplicates from dict

def remove_duplicate(dup_dict):
    new_dict = {}
    temp = []
    for key, value in dup_dict.items():
        if value not in temp:
            new_dict[key] = value
    return new_dict

    
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"brand": "Ford"}

print(remove_duplicate(car))


# 10. Write a Python program to sum all the items in a dictionary.
def dict_sum(sample_dict):
    empty_int_ = int()
    for value in sample_dict.values():
        empty_int_ += value

    return empty_int_



car = {
"brand": 1,
"model": 2,
"year": 12,
"brand": 4}

print(dict_sum(car))