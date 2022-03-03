#Merge two dictionaries.
dict1 = {"Name": "Allen", "Age": "21"}
dict2 = {"College": "AJCE", "Department": "MCA"}
dict3 = {}
print(dict1)
print(dict2)
dict3.update(dict1)
dict3.update(dict2)
print(dict3)