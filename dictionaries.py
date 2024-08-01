dic = {
    "name": "Ayush Jain",
    "age": 22,
    "eligible": True
}
# print(dic)
# print(dic['name'])
# print(dic.get('name'))
# print(dic.keys())
# print(dic.values())
# print(dic.items())

# for key , values in dic.items():
#     print(f"the value corresponding to {key} is {values}")


# dictionaries method

info ={
    "name": "ayush jain",
    "age": 21,
    "email": "ayushabhi094@gmail.com",
    "eligible": True
}
info2 = {
    "phone no": 9479640518
}

info.update({"age": 19})
info.update({"eligible":False})
info.update(info2)

info.pop('eligible')  #remove last key-value pair by giving key
info.popitem()  #remove last key-value pair
del info['email']  
print(info)

