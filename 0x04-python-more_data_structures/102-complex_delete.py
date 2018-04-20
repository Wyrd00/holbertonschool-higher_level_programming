#!/usr/bin/python3
def complex_delete(a_dictionary, value):
        for k in dict(a_dictionary):
                if value == a_dictionary[k]:
                        del a_dictionary[k]
        return a_dictionary
# make copy of dict b/c deleting a key will mess the loop-so loop
#through copy, delete & return OP
