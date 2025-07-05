# # Dictionory in python
# # A dictionary is a collection of key-value pairs, where each key is unique and maps to a value.
# # dict1 ={}
# # print(dict1)

# dict2={}
# dict2['name'] = 'snehdeep'
# dict2['age'] = 20
# dict2['skills'] = ['python','sql']
# dict2['states_visited'] = ['telangana','mp','up','bihar']
# dict2['other details']={'nationality' : 'indian','color' : 'black'}
# print(dict2)

# # to check the lengtn of dict
# print(len(dict2))

# # to access perticular key value
# # print(dict2['name'])
# # to accses the list in dict
# # print(dict2['states_visited'][0])

# #  to acces a dictionory within dictionory
# print(dict2['other details']['color'])

# the concept of dictionary within a dictionary is also called nested dictionary
students = {
    "student1": {
        "name": "snehdeep",
        "age": 20,
        "marks": {
            "math": 90,
            "science": 85
        }
    },
    "student2": {
        "name": "guddu",
        "age": 21,
        "marks": {
            "math": 95,
            "science": 88
        }
    }
}
print(students["student1"]["marks"]["math"])
