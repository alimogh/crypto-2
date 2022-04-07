""" test_dict_elm_is_none :
    4/7/2022 12:57 PM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

d1 = {"id":None}
print(d1["id"] if d1["id"] else "NOT")
d2 = {"id":"abc123"}
print(d2["id"] if d2["id"] else "NOT")


